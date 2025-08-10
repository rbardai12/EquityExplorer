@echo off
echo Starting EquityExplorer Frontend...
echo.

REM Check if virtual environment exists
if not exist "..\venv" (
    echo Virtual environment not found. Creating one...
    cd ..
    python -m venv venv
    cd frontend
)

REM Activate virtual environment
echo Activating virtual environment...
call ..\venv\Scripts\activate.bat

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not available in virtual environment
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Installing required dependencies...
    pip install -r ..\requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Start the frontend
echo Starting Flask application...
echo Frontend will be available at: http://localhost:5001 (or next available port)
python start_frontend.py

pause 