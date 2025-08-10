#!/usr/bin/env python3
"""
Frontend startup script for EquityExplorer
This script handles the proper setup and startup of the Flask web application
"""

import os
import sys
import logging
from pathlib import Path

# Add parent directory to path for imports
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_dependencies():
    """Check if all required dependencies are available"""
    try:
        import flask
        import flask_cors
        import pandas
        logger.info("All required dependencies are available")
        return True
    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        logger.error("Please install required dependencies with: pip install -r requirements.txt")
        return False

def check_config():
    """Check if configuration is properly set up"""
    try:
        from config import Config
        logger.info("Configuration loaded successfully")
        return True
    except ImportError as e:
        logger.error(f"Configuration error: {e}")
        return False

def create_directories():
    """Create necessary directories if they don't exist"""
    try:
        from config import Config
        Config.create_directories()
        logger.info("Directories created/verified successfully")
        return True
    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        return False

def find_available_port(start_port=5001, max_attempts=10):
    """Find an available port starting from start_port"""
    import socket
    
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    
    return start_port  # Fallback to start_port if all are busy

def main():
    """Main startup function"""
    logger.info("Starting EquityExplorer Frontend...")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check configuration
    if not check_config():
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        sys.exit(1)
    
    # Import and start Flask app
    try:
        from app import app
        logger.info("Flask application imported successfully")
        
        # Find available port
        port = find_available_port()
        host = os.environ.get('HOST', '0.0.0.0')
        
        logger.info(f"Starting Flask server on {host}:{port}")
        logger.info(f"Open your browser to: http://localhost:{port}")
        
        # Start the Flask app
        app.run(
            host=host,
            port=port,
            debug=True,
            use_reloader=True
        )
        
    except Exception as e:
        logger.error(f"Failed to start Flask application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 