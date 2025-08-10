import os
import platform
import subprocess
import logging
import time
from pathlib import Path
from typing import Dict, Optional
from config import Config

logger = logging.getLogger(__name__)

class BatchScriptManager:
    """Manages batch script operations in a cross-platform way"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.is_windows = self.system == 'windows'
        
    def update_batch_script(self, script_name: str, ticker: str, file_path: Path, 
                           statement_type: str = None) -> Path:
        """
        Update a batch script with new file paths and ticker information
        
        Args:
            script_name: Name of the batch script to update
            ticker: Stock ticker symbol
            file_path: Path to the file to be processed
            statement_type: Type of financial statement (for process naming)
            
        Returns:
            Path to updated batch script
        """
        script_path = Config.BASE_DIR / 'scripts' / script_name
        
        if not script_path.exists():
            raise FileNotFoundError(f"Batch script not found: {script_path}")
        
        try:
            # Read the original script
            with open(script_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Update the script content
            updated_lines = []
            for i, line in enumerate(lines):
                if 'set FileName=' in line:
                    # Update filename
                    if statement_type:
                        new_line = f'set FileName="{ticker} {statement_type}.csv"\n'
                    else:
                        new_line = f'set FileName="{file_path.name}"\n'
                    updated_lines.append(new_line)
                elif 'set FilePath=' in line:
                    # Update file path
                    new_line = f'set FilePath="{file_path.absolute()}"\n'
                    updated_lines.append(new_line)
                elif 'set ProcessName=' in line and statement_type:
                    # Update process name if statement type is provided
                    process_name = Config.PROCESS_NAMES.get(statement_type.lower().replace(' ', '_'), 'Load Data')
                    new_line = f'set ProcessName="{process_name}"\n'
                    updated_lines.append(new_line)
                else:
                    updated_lines.append(line)
            
            # Write updated script
            with open(script_path, 'w', encoding='utf-8') as f:
                f.writelines(updated_lines)
            
            logger.info(f"Updated batch script {script_name} for ticker {ticker}")
            return script_path
            
        except Exception as e:
            logger.error(f"Error updating batch script {script_name}: {e}")
            raise
    
    def execute_batch_script(self, script_path: Path, wait: bool = True) -> Optional[subprocess.Popen]:
        """
        Execute a batch script
        
        Args:
            script_path: Path to the batch script
            wait: Whether to wait for execution to complete
            
        Returns:
            Subprocess object if not waiting, None otherwise
        """
        try:
            if self.is_windows:
                # Windows: use start command
                cmd = ["start", "cmd", "/k", str(script_path)]
                process = subprocess.Popen(cmd, shell=True)
            else:
                # Unix-like systems: execute directly
                if script_path.suffix == '.bat':
                    # Convert .bat to .sh if needed
                    sh_script = script_path.with_suffix('.sh')
                    if sh_script.exists():
                        script_path = sh_script
                
                # Make script executable
                os.chmod(script_path, 0o755)
                process = subprocess.Popen([str(script_path)], shell=True)
            
            if wait:
                process.wait()
                logger.info(f"Executed batch script {script_path.name}")
                return None
            else:
                logger.info(f"Started batch script {script_path.name}")
                return process
                
        except Exception as e:
            logger.error(f"Error executing batch script {script_path.name}: {e}")
            raise
    
    def execute_statement_scripts(self, ticker: str, file_paths: Dict[str, Path]) -> None:
        """
        Execute all statement processing scripts for a ticker
        
        Args:
            ticker: Stock ticker symbol
            file_paths: Dictionary mapping statement types to file paths
        """
        script_mapping = {
            'balance_sheet': Config.BATCH_SCRIPTS['balance_sheet'],
            'income_statement': Config.BATCH_SCRIPTS['income_statement'],
            'cash_flow': Config.BATCH_SCRIPTS['cash_flow']
        }
        
        processes = []
        
        for statement_type, file_path in file_paths.items():
            if statement_type in script_mapping:
                script_name = script_mapping[statement_type]
                
                try:
                    # Update the batch script
                    updated_script = self.update_batch_script(
                        script_name, 
                        ticker, 
                        file_path, 
                        statement_type
                    )
                    
                    # Execute the script
                    process = self.execute_batch_script(updated_script, wait=False)
                    if process:
                        processes.append(process)
                    
                    # Small delay between script executions
                    time.sleep(2)
                    
                except Exception as e:
                    logger.error(f"Failed to execute {statement_type} script for {ticker}: {e}")
        
        # Wait for all processes to complete
        for process in processes:
            try:
                process.wait()
            except Exception as e:
                logger.error(f"Error waiting for process: {e}")
        
        logger.info(f"Completed all statement scripts for {ticker}")
    
    def execute_utility_scripts(self) -> None:
        """Execute utility scripts for stocks and date data"""
        try:
            # Execute stocks script
            stocks_script = Config.BATCH_SCRIPTS['stocks']
            stocks_path = Config.BASE_DIR / 'Stocks.csv'
            
            if stocks_path.exists():
                updated_script = self.update_batch_script(stocks_script, 'Stocks', stocks_path)
                self.execute_batch_script(updated_script, wait=True)
            
            # Execute date script
            date_script = Config.BATCH_SCRIPTS['date']
            date_path = Config.BASE_DIR / 'Today Date.csv'
            
            if date_path.exists():
                updated_script = self.update_batch_script(date_script, 'Date', date_path)
                self.execute_batch_script(updated_script, wait=True)
                
        except Exception as e:
            logger.error(f"Error executing utility scripts: {e}")
            raise 