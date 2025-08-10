# Example configuration file - copy this to config.py and fill in your values
import os
from pathlib import Path

class Config:
    """Configuration class for EquityExplorer"""
    
    # API Configuration
    FINANCIAL_MODELING_PREP_API_KEY = 'your_api_key_here'  # Get from https://financialmodelingprep.com/
    FINANCIAL_MODELING_PREP_BASE_URL = 'https://financialmodelingprep.com/api/v3'
    
    # Anaplan Configuration
    ANAPLAN_SERVICE_URL = 'https://api.anaplan.com'
    ANAPLAN_AUTH_URL = 'https://auth.anaplan.com'
    ANAPLAN_USER = 'your_username'
    ANAPLAN_WORKSPACE_ID = 'your_workspace_id'
    ANAPLAN_MODEL_ID = 'your_model_id'
    
    # File Paths
    BASE_DIR = Path(__file__).parent
    OUTPUT_DIR = BASE_DIR / 'output'
    TEMPLATE_DIR = BASE_DIR / 'templates'
    
    # Batch Script Templates
    BATCH_SCRIPTS = {
        'balance_sheet': 'Basic Auth Process Script.bat',
        'income_statement': 'Basic Auth Process Script2.bat',
        'cash_flow': 'Basic Auth Process Script3.bat',
        'stocks': 'Basic Auth Process Script4.bat',
        'date': 'Basic Auth Process Script5.bat'
    }
    
    # Process Names
    PROCESS_NAMES = {
        'balance_sheet': 'Load Balance Sheet',
        'income_statement': 'Load Income Statement',
        'cash_flow': 'Load Cash Flow',
        'stocks': 'Load Stocks',
        'date': 'Load Date'
    }
    
    # Stock List (S&P 500) - customize as needed
    DEFAULT_STOCKS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    
    # Retry Configuration
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds
    
    # File Processing
    CHUNK_SIZE = 1
    
    @classmethod
    def create_directories(cls):
        """Create necessary directories if they don't exist"""
        cls.OUTPUT_DIR.mkdir(exist_ok=True)
        cls.TEMPLATE_DIR.mkdir(exist_ok=True)
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is set"""
        required_vars = [
            'FINANCIAL_MODELING_PREP_API_KEY',
            'ANAPLAN_USER',
            'ANAPLAN_WORKSPACE_ID',
            'ANAPLAN_MODEL_ID'
        ]
        
        missing_vars = [var for var in required_vars if not getattr(cls, var) or getattr(cls, var) == 'your_api_key_here']
        
        if missing_vars:
            raise ValueError(f"Missing required configuration variables: {', '.join(missing_vars)}")
        
        return True 