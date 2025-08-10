import csv
import logging
from pathlib import Path
from typing import List, Dict
from config import Config

logger = logging.getLogger(__name__)

class CSVProcessor:
    """Handles CSV file processing and cleaning operations"""
    
    @staticmethod
    def remove_column(input_file: Path, output_file: Path, column_index: int) -> Path:
        """
        Remove a specific column from a CSV file
        
        Args:
            input_file: Path to input CSV file
            output_file: Path to output CSV file
            column_index: Index of column to remove
            
        Returns:
            Path to processed file
        """
        try:
            with open(input_file, 'r', newline='', encoding='utf-8') as source:
                reader = csv.reader(source)
                
                with open(output_file, 'w', newline='', encoding='utf-8') as result:
                    writer = csv.writer(result)
                    
                    for row in reader:
                        if len(row) > column_index:
                            del row[column_index]
                        writer.writerow(row)
            
            logger.info(f"Removed column {column_index} from {input_file.name}")
            return output_file
            
        except Exception as e:
            logger.error(f"Error processing {input_file.name}: {e}")
            raise
    
    @staticmethod
    def replace_text_in_file(file_path: Path, old_text: str, new_text: str) -> None:
        """
        Replace text in a file
        
        Args:
            file_path: Path to file to modify
            old_text: Text to replace
            new_text: New text to insert
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_text in content:
                content = content.replace(old_text, new_text)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                logger.info(f"Replaced '{old_text}' with '{new_text}' in {file_path.name}")
            else:
                logger.warning(f"Text '{old_text}' not found in {file_path.name}")
                
        except Exception as e:
            logger.error(f"Error replacing text in {file_path.name}: {e}")
            raise
    
    @staticmethod
    def process_statement_files(ticker: str, base_dir: Path) -> Dict[str, Path]:
        """
        Process all statement files for a ticker
        
        Args:
            ticker: Stock ticker symbol
            base_dir: Base directory containing the files
            
        Returns:
            Dictionary mapping statement types to processed file paths
        """
        statements = ['balance_sheet', 'cash_flow', 'income_statement']
        processed_files = {}
        
        for statement in statements:
            input_file = base_dir / f"{ticker} {statement}.csv"
            output_file = base_dir / f"{ticker} {statement} New.csv"
            
            if input_file.exists():
                try:
                    # Remove first column (index 0)
                    processed_file = CSVProcessor.remove_column(input_file, output_file, 0)
                    processed_files[statement] = processed_file
                    
                    # Replace ticker reference in Income Statement
                    if statement == 'income_statement':
                        CSVProcessor.replace_text_in_file(
                            input_file, 
                            ticker, 
                            "Ticker:"
                        )
                        
                except Exception as e:
                    logger.error(f"Failed to process {statement} for {ticker}: {e}")
                    processed_files[statement.lower().replace(' ', '_')] = input_file
            else:
                logger.warning(f"File not found: {input_file}")
        
        return processed_files
    
    @staticmethod
    def convert_excel_to_csv(excel_file: Path, csv_file: Path) -> Path:
        """
        Convert Excel file to CSV format
        
        Args:
            excel_file: Path to Excel file
            csv_file: Path to output CSV file
            
        Returns:
            Path to created CSV file
        """
        try:
            import pandas as pd
            
            # Read Excel file
            df = pd.read_excel(excel_file)
            
            # Save as CSV
            df.to_csv(csv_file, index=False, header=True)
            
            logger.info(f"Converted {excel_file.name} to {csv_file.name}")
            return csv_file
            
        except ImportError:
            logger.error("pandas is required for Excel to CSV conversion")
            raise
        except Exception as e:
            logger.error(f"Error converting {excel_file.name} to CSV: {e}")
            raise 