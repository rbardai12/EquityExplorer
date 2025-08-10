#!/usr/bin/env python3
"""
Test script to verify EquityExplorer setup
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test if all modules can be imported"""
    print("Testing imports...")
    
    try:
        from config import Config
        print("✓ Config module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Config: {e}")
        return False
    
    try:
        from financial_data_fetcher import FinancialDataFetcher
        print("✓ FinancialDataFetcher module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import FinancialDataFetcher: {e}")
        return False
    
    try:
        from csv_processor import CSVProcessor
        print("✓ CSVProcessor module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import CSVProcessor: {e}")
        return False
    
    try:
        from batch_script_manager import BatchScriptManager
        print("✓ BatchScriptManager module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import BatchScriptManager: {e}")
        return False
    
    try:
        from equity_explorer import EquityExplorer
        print("✓ EquityExplorer module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import EquityExplorer: {e}")
        return False
    
    return True

def test_config():
    """Test configuration setup"""
    print("\nTesting configuration...")
    
    try:
        from config import Config
        
        # Test directory creation
        Config.create_directories()
        print("✓ Directories created successfully")
        
        # Test configuration validation (should fail with default values)
        try:
            Config.validate_config()
            print("✓ Configuration validation passed")
        except ValueError as e:
            print(f"⚠ Configuration validation failed (expected): {e}")
            print("  This is normal - you need to set your API keys in config.py")
        
        return True
        
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False

def test_file_structure():
    """Test if required files exist"""
    print("\nTesting file structure...")
    
    required_files = [
        'config.py',
        'financial_data_fetcher.py',
        'csv_processor.py',
        'batch_script_manager.py',
        'equity_explorer.py',
        'cli.py',
        'requirements.txt'
    ]
    
    missing_files = []
    for file in required_files:
        if Path(file).exists():
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            missing_files.append(file)
    
    if missing_files:
        print(f"\nMissing files: {', '.join(missing_files)}")
        return False
    
    return True

def test_dependencies():
    """Test if required dependencies are available"""
    print("\nTesting dependencies...")
    
    try:
        import requests
        print("✓ requests module available")
    except ImportError:
        print("✗ requests module not available - run: pip install requests")
        return False
    
    try:
        import pandas
        print("✓ pandas module available")
    except ImportError:
        print("✗ pandas module not available - run: pip install pandas")
        return False
    
    try:
        import openpyxl
        print("✓ openpyxl module available")
    except ImportError:
        print("✗ openpyxl module not available - run: pip install openpyxl")
        return False
    
    return True

def main():
    """Run all tests"""
    print("EquityExplorer Setup Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_config,
        test_file_structure,
        test_dependencies
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! EquityExplorer is ready to use.")
        print("\nNext steps:")
        print("1. Copy config.example.py to config.py")
        print("2. Edit config.py with your API keys and Anaplan credentials")
        print("3. Run: python cli.py ticker AAPL")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 