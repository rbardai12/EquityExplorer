#!/usr/bin/env python3
"""
Test script for EquityExplorer Frontend
This script verifies that all components are properly configured
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import flask
        print(f"✓ Flask {flask.__version__}")
    except ImportError as e:
        print(f"✗ Flask import failed: {e}")
        return False
    
    try:
        import flask_cors
        print("✓ Flask-CORS")
    except ImportError as e:
        print(f"✗ Flask-CORS import failed: {e}")
        return False
    
    try:
        import pandas
        print(f"✓ Pandas {pandas.__version__}")
    except ImportError as e:
        print(f"✗ Pandas import failed: {e}")
        return False
    
    return True

def test_paths():
    """Test if required paths and files exist"""
    print("\nTesting paths...")
    
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    
    # Check if parent directory exists
    if parent_dir.exists():
        print(f"✓ Parent directory: {parent_dir}")
    else:
        print(f"✗ Parent directory not found: {parent_dir}")
        return False
    
    # Check if config.py exists
    config_file = parent_dir / "config.py"
    if config_file.exists():
        print(f"✓ Config file: {config_file}")
    else:
        print(f"✗ Config file not found: {config_file}")
        return False
    
    # Check if equity_explorer.py exists
    equity_file = parent_dir / "equity_explorer.py"
    if equity_file.exists():
        print(f"✓ EquityExplorer: {equity_file}")
    else:
        print(f"✗ EquityExplorer not found: {equity_file}")
        return False
    
    return True

def test_config():
    """Test if configuration can be loaded"""
    print("\nTesting configuration...")
    
    try:
        # Add parent directory to path
        current_dir = Path(__file__).parent
        parent_dir = current_dir.parent
        sys.path.insert(0, str(parent_dir))
        
        from config import Config
        print("✓ Configuration loaded successfully")
        
        # Test directory creation
        try:
            Config.create_directories()
            print("✓ Directories created/verified")
        except Exception as e:
            print(f"✗ Directory creation failed: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False

def test_flask_app():
    """Test if Flask app can be created"""
    print("\nTesting Flask app...")
    
    try:
        # Add parent directory to path
        current_dir = Path(__file__).parent
        parent_dir = current_dir.parent
        sys.path.insert(0, str(parent_dir))
        
        from app import app
        print("✓ Flask app imported successfully")
        
        # Test basic app properties
        if hasattr(app, 'name'):
            print(f"✓ App name: {app.name}")
        else:
            print("✗ App missing name attribute")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Flask app test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("EquityExplorer Frontend Test Suite")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_paths,
        test_config,
        test_flask_app
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Frontend is ready to use.")
        print("\nTo start the frontend:")
        print("  Windows: start_frontend.bat")
        print("  macOS/Linux: ./start_frontend.sh")
        print("  Manual: python start_frontend.py")
        return 0
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 