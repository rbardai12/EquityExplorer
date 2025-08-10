#!/bin/bash

echo "Starting EquityExplorer Frontend..."
echo

# Check if virtual environment exists
if [ ! -d "../venv" ]; then
    echo "Virtual environment not found. Creating one..."
    cd ..
    python3 -m venv venv
    cd frontend
fi

# Activate virtual environment
echo "Activating virtual environment..."
source ../venv/bin/activate

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "Error: Python is not available in virtual environment"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
if ! python -c "import flask" &> /dev/null; then
    echo "Installing required dependencies..."
    pip install -r ../requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
fi

# Make the startup script executable
chmod +x start_frontend.py

# Start the frontend
echo "Starting Flask application..."
echo "Frontend will be available at: http://localhost:5001 (or next available port)"
python start_frontend.py 