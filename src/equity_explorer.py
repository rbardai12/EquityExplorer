import logging
import time
from pathlib import Path
from typing import List, Dict
from config import Config
from src.financial_data_fetcher import FinancialDataFetcher
from src.csv_processor import CSVProcessor
from src.batch_script_manager import BatchScriptManager

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('equity_explorer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EquityExplorer:
    """Main orchestrator class for EquityExplorer"""
    
    def __init__(self):
        """Initialize the EquityExplorer"""
        try:
            # Validate configuration
            Config.validate_config()
            Config.create_directories()
            
            # Initialize components
            self.data_fetcher = FinancialDataFetcher()
            self.csv_processor = CSVProcessor()
            self.batch_manager = BatchScriptManager()
            
            logger.info("EquityExplorer initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize EquityExplorer: {e}")
            # For basic usage without Anaplan, we can continue
            if "ANAPLAN" in str(e):
                logger.warning("Anaplan configuration missing - continuing with basic functionality")
                # Initialize with basic components only
                self.data_fetcher = FinancialDataFetcher()
                self.csv_processor = CSVProcessor()
                self.batch_manager = None  # No batch processing without Anaplan
                logger.info("EquityExplorer initialized with basic functionality (no Anaplan)")
            else:
                raise
    
    def process_single_ticker(self, ticker: str) -> Dict[str, Path]:
        """
        Process a single ticker completely
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dictionary mapping statement types to processed file paths
        """
        logger.info(f"Starting processing for ticker: {ticker}")
        
        try:
            # Step 1: Fetch financial data
            logger.info(f"Fetching financial data for {ticker}")
            file_paths = self.data_fetcher.process_ticker(ticker)
            
            if not file_paths:
                logger.error(f"No data fetched for {ticker}")
                return {}
            
            # Step 2: Process CSV files
            logger.info(f"Processing CSV files for {ticker}")
            processed_files = self.csv_processor.process_statement_files(
                ticker, 
                Config.OUTPUT_DIR
            )
            
            # Step 3: Execute batch scripts (if Anaplan is configured)
            if self.batch_manager:
                logger.info(f"Executing batch scripts for {ticker}")
                self.batch_manager.execute_statement_scripts(ticker, processed_files)
            else:
                logger.info(f"Skipping batch scripts for {ticker} (Anaplan not configured)")
            
            logger.info(f"Completed processing for {ticker}")
            return processed_files
            
        except Exception as e:
            logger.error(f"Error processing ticker {ticker}: {e}")
            return {}
    
    def process_multiple_tickers(self, tickers: List[str]) -> Dict[str, Dict[str, Path]]:
        """
        Process multiple tickers
        
        Args:
            tickers: List of stock ticker symbols
            
        Returns:
            Dictionary mapping tickers to their processed file paths
        """
        logger.info(f"Starting batch processing for {len(tickers)} tickers")
        
        results = {}
        
        for i, ticker in enumerate(tickers, 1):
            logger.info(f"Processing ticker {i}/{len(tickers)}: {ticker}")
            
            try:
                file_paths = self.process_single_ticker(ticker)
                results[ticker] = file_paths
                
                # Add delay between tickers to be respectful to APIs
                if i < len(tickers):
                    time.sleep(Config.RETRY_DELAY)
                    
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                results[ticker] = {}
        
        logger.info(f"Completed batch processing. Successfully processed {len([r for r in results.values() if r])} tickers")
        return results
    
    def process_utility_files(self) -> None:
        """Process utility files (stocks and date)"""
        logger.info("Processing utility files")
        
        try:
            # Convert Excel files to CSV if they exist
            excel_files = {
                'Stocks.xlsx': 'Stocks.csv',
                'Today Date.xlsx': 'Today Date.csv'
            }
            
            for excel_file, csv_file in excel_files.items():
                excel_path = Config.BASE_DIR / excel_file
                csv_path = Config.BASE_DIR / csv_file
                
                if excel_path.exists():
                    logger.info(f"Converting {excel_file} to CSV")
                    self.csv_processor.convert_excel_to_csv(excel_path, csv_path)
                elif not csv_path.exists():
                    logger.warning(f"Neither {excel_file} nor {csv_file} found")
            
            # Execute utility scripts (if batch manager is available)
            if self.batch_manager:
                self.batch_manager.execute_utility_scripts()
            else:
                logger.info("Skipping utility scripts (batch manager not available)")
            
            logger.info("Utility files processed successfully")
            
        except Exception as e:
            logger.error(f"Error processing utility files: {e}")
            raise
    
    def run_full_analysis(self, tickers: List[str] = None) -> Dict[str, Dict[str, Path]]:
        """
        Run the complete equity analysis pipeline
        
        Args:
            tickers: List of stock ticker symbols. If None, uses default stocks from config
            
        Returns:
            Dictionary mapping tickers to their processed file paths
        """
        if tickers is None:
            tickers = Config.DEFAULT_STOCKS
        
        logger.info(f"Starting full equity analysis for {len(tickers)} tickers")
        
        try:
            # Process all tickers
            results = self.process_multiple_tickers(tickers)
            
            # Process utility files
            self.process_utility_files()
            
            logger.info("Full equity analysis completed successfully")
            return results
            
        except Exception as e:
            logger.error(f"Full equity analysis failed: {e}")
            raise
    
    def run_single_ticker_analysis(self, ticker: str) -> Dict[str, Path]:
        """
        Run analysis for a single ticker
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dictionary mapping statement types to processed file paths
        """
        logger.info(f"Starting single ticker analysis for {ticker}")
        
        try:
            results = self.process_single_ticker(ticker)
            
            # Process utility files
            self.process_utility_files()
            
            logger.info(f"Single ticker analysis completed for {ticker}")
            return results
            
        except Exception as e:
            logger.error(f"Single ticker analysis failed for {ticker}: {e}")
            raise


def main():
    """Main entry point"""
    try:
        # Initialize EquityExplorer
        explorer = EquityExplorer()
        
        # Example usage - process a single ticker
        ticker = 'AAPL'  # You can change this or make it configurable
        results = explorer.run_single_ticker_analysis(ticker)
        
        if results:
            logger.info(f"Successfully processed {ticker}")
            for statement_type, file_path in results.items():
                logger.info(f"  {statement_type}: {file_path}")
        else:
            logger.error(f"Failed to process {ticker}")
            
    except Exception as e:
        logger.error(f"Application failed: {e}")
        raise


if __name__ == "__main__":
    main() 