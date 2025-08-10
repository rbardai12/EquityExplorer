import requests
import time
import logging
from pathlib import Path
from typing import List, Dict, Optional
from config import Config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FinancialDataFetcher:
    """Handles fetching financial data from Financial Modeling Prep API"""
    
    def __init__(self):
        self.api_key = Config.FINANCIAL_MODELING_PREP_API_KEY
        self.base_url = Config.FINANCIAL_MODELING_PREP_BASE_URL
        self.session = requests.Session()
        
    def fetch_financial_statement(self, ticker: str, statement_type: str) -> Optional[bytes]:
        """
        Fetch financial statement data for a given ticker
        
        Args:
            ticker: Stock ticker symbol
            statement_type: Type of statement ('income-statement', 'cash-flow-statement', 'balance-sheet-statement')
            
        Returns:
            Response content as bytes or None if failed
        """
        url = f"{self.base_url}/{statement_type}/{ticker}"
        params = {
            'datatype': 'csv',
            'apikey': self.api_key
        }
        
        for attempt in range(Config.MAX_RETRIES):
            try:
                logger.info(f"Fetching {statement_type} for {ticker} (attempt {attempt + 1})")
                response = self.session.get(url, params=params, timeout=30)
                response.raise_for_status()
                
                # Check if response contains error message
                if 'contact' in response.text.lower():
                    logger.warning(f"API returned error message for {ticker} {statement_type}")
                    if attempt < Config.MAX_RETRIES - 1:
                        time.sleep(Config.RETRY_DELAY)
                        continue
                    return None
                
                logger.info(f"Successfully fetched {statement_type} for {ticker}")
                return response.content
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching {statement_type} for {ticker}: {e}")
                if attempt < Config.MAX_RETRIES - 1:
                    time.sleep(Config.RETRY_DELAY)
                    continue
                return None
        
        return None
    
    def fetch_all_statements(self, ticker: str) -> Dict[str, Optional[bytes]]:
        """
        Fetch all three financial statements for a ticker
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dictionary with statement types as keys and content as values
        """
        statements = {
            'income_statement': 'income-statement',
            'cash_flow': 'cash-flow-statement',
            'balance_sheet': 'balance-sheet-statement'
        }
        
        results = {}
        for name, endpoint in statements.items():
            content = self.fetch_financial_statement(ticker, endpoint)
            results[name] = content
            
        return results
    
    def save_statement(self, ticker: str, statement_type: str, content: bytes) -> Path:
        """
        Save financial statement content to a CSV file
        
        Args:
            ticker: Stock ticker symbol
            statement_type: Type of statement
            content: File content as bytes
            
        Returns:
            Path to saved file
        """
        Config.create_directories()
        filename = f"{ticker} {statement_type}.csv"
        filepath = Config.OUTPUT_DIR / filename
        
        with open(filepath, 'wb') as f:
            f.write(content)
        
        logger.info(f"Saved {filename} to {filepath}")
        return filepath
    
    def process_ticker(self, ticker: str) -> Dict[str, Path]:
        """
        Process a single ticker by fetching and saving all statements
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            Dictionary mapping statement types to file paths
        """
        logger.info(f"Processing ticker: {ticker}")
        
        # Fetch all statements
        statements = self.fetch_all_statements(ticker)
        
        # Save statements and collect file paths
        file_paths = {}
        for statement_type, content in statements.items():
            if content:
                filepath = self.save_statement(ticker, statement_type, content)
                file_paths[statement_type] = filepath
            else:
                logger.error(f"Failed to fetch {statement_type} for {ticker}")
        
        return file_paths
    
    def process_tickers(self, tickers: List[str]) -> Dict[str, Dict[str, Path]]:
        """
        Process multiple tickers
        
        Args:
            tickers: List of stock ticker symbols
            
        Returns:
            Dictionary mapping tickers to their statement file paths
        """
        results = {}
        
        for ticker in tickers:
            try:
                file_paths = self.process_ticker(ticker)
                results[ticker] = file_paths
                
                # Add delay between requests to be respectful to API
                time.sleep(1)
                
            except Exception as e:
                logger.error(f"Error processing ticker {ticker}: {e}")
                results[ticker] = {}
        
        return results 