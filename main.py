#!/usr/bin/env python3
"""
Main entry point for EquityExplorer
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from equity_explorer import EquityExplorer
from config import Config

def main():
    """Main application entry point"""
    print("🚀 EquityExplorer - Financial Data Analysis Tool")
    print("=" * 50)
    
    try:
        # Initialize the explorer
        explorer = EquityExplorer()
        print("✅ EquityExplorer initialized successfully")
        
        # Show available options
        print("\nAvailable actions:")
        print("1. Run full analysis with default stocks")
        print("2. Process specific ticker")
        print("3. Start web interface")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n🔄 Running full analysis...")
            results = explorer.run_full_analysis()
            success_count = len([r for r in results.values() if r])
            total_count = len(results)
            print(f"✅ Analysis complete: {success_count}/{total_count} tickers processed")
            
        elif choice == "2":
            ticker = input("Enter ticker symbol: ").strip().upper()
            if ticker:
                print(f"\n🔄 Processing {ticker}...")
                results = explorer.run_single_ticker_analysis(ticker)
                if results:
                    print(f"✅ {ticker} processed successfully")
                    for statement_type, file_path in results.items():
                        print(f"  {statement_type}: {file_path}")
                else:
                    print(f"❌ Failed to process {ticker}")
            else:
                print("❌ Invalid ticker symbol")
                
        elif choice == "3":
            print("\n🌐 Starting web interface...")
            print("Please run: python frontend/app.py")
            
        elif choice == "4":
            print("👋 Goodbye!")
            return
            
        else:
            print("❌ Invalid choice")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 