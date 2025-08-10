#!/usr/bin/env python3
"""
Frontend-specific configuration for EquityExplorer
"""

import os
from pathlib import Path

class FrontendConfig:
    """Configuration class for the frontend application"""
    
    # Server settings
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    
    # Development settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'true').lower() == 'true'
    ENV = os.environ.get('FLASK_ENV', 'development')
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    # CORS settings
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')
    
    # Auto-refresh interval (seconds)
    STATUS_REFRESH_INTERVAL = 30
    
    # File display settings
    MAX_ROWS_DISPLAY = 100
    MAX_FILE_SIZE_MB = 50
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    @classmethod
    def get_server_url(cls):
        """Get the server URL for display purposes"""
        if cls.HOST == '0.0.0.0':
            return f"http://localhost:{cls.PORT}"
        return f"http://{cls.HOST}:{cls.PORT}"
    
    @classmethod
    def validate(cls):
        """Validate configuration settings"""
        errors = []
        
        if cls.PORT < 1 or cls.PORT > 65535:
            errors.append(f"Invalid port number: {cls.PORT}")
        
        if cls.STATUS_REFRESH_INTERVAL < 5:
            errors.append(f"Status refresh interval too low: {cls.STATUS_REFRESH_INTERVAL}")
        
        if cls.MAX_ROWS_DISPLAY < 10:
            errors.append(f"Max rows display too low: {cls.MAX_ROWS_DISPLAY}")
        
        return errors 