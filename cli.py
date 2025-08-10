#!/usr/bin/env python3
"""
Command Line Interface for EquityExplorer
"""

import argparse
import sys
import logging
from typing import List
from src.equity_explorer import EquityExplorer
from config import Config

def setup_logging(verbose: bool = False):
    """Setup logging configuration"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('equity_explorer.log'),
            logging.StreamHandler()
        ]
    )

def process_single_ticker(ticker: str, verbose: bool = False):
    """Process a single ticker"""
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    
    try:
        explorer = EquityExplorer()
        results = explorer.run_single_ticker_analysis(ticker)
        
        if results:
            logger.info(f"Successfully processed {ticker}")
            for statement_type, file_path in results.items():
                logger.info(f"  {statement_type}: {file_path}")
            return True
        else:
            logger.error(f"Failed to process {ticker}")
            return False
            
    except Exception as e:
        logger.error(f"Error processing {ticker}: {e}")
        return False

def process_multiple_tickers(tickers: List[str], verbose: bool = False):
    """Process multiple tickers"""
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    
    try:
        explorer = EquityExplorer()
        results = explorer.process_multiple_tickers(tickers)
        
        success_count = len([r for r in results.values() if r])
        logger.info(f"Successfully processed {success_count}/{len(tickers)} tickers")
        
        for ticker, result in results.items():
            if result:
                logger.info(f"✓ {ticker}: {len(result)} statements processed")
            else:
                logger.warning(f"✗ {ticker}: failed to process")
        
        return success_count == len(tickers)
        
    except Exception as e:
        logger.error(f"Error processing tickers: {e}")
        return False

def run_full_analysis(verbose: bool = False):
    """Run full analysis with default stocks"""
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    
    try:
        explorer = EquityExplorer()
        results = explorer.run_full_analysis()
        
        success_count = len([r for r in results.values() if r])
        total_count = len(results)
        
        logger.info(f"Full analysis completed: {success_count}/{total_count} tickers processed successfully")
        return success_count == total_count
        
    except Exception as e:
        logger.error(f"Full analysis failed: {e}")
        return False

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='EquityExplorer - Financial Data Analysis Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process a single ticker
  python cli.py ticker AAPL
  
  # Process multiple tickers
  python cli.py tickers AAPL MSFT GOOGL
  
  # Run full analysis with default stocks
  python cli.py full
  
  # Verbose output
  python cli.py --verbose ticker AAPL
        """
    )
    
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Enable verbose logging')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Single ticker command
    ticker_parser = subparsers.add_parser('ticker', help='Process a single ticker')
    ticker_parser.add_argument('symbol', help='Stock ticker symbol')
    
    # Multiple tickers command
    tickers_parser = subparsers.add_parser('tickers', help='Process multiple tickers')
    tickers_parser.add_argument('symbols', nargs='+', help='Stock ticker symbols')
    
    # Full analysis command
    full_parser = subparsers.add_parser('full', help='Run full analysis with default stocks')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        success = False
        
        if args.command == 'ticker':
            success = process_single_ticker(args.symbol, args.verbose)
        elif args.command == 'tickers':
            success = process_multiple_tickers(args.symbols, args.verbose)
        elif args.command == 'full':
            success = run_full_analysis(args.verbose)
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 