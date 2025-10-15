@echo off
REM Startup script for Meeting Summarizer Backend

echo ========================================
echo Meeting Summarizer - Backend Startup
echo ========================================
echo.

cd backend

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Check if requirements are installed
echo Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
) else (
    echo Dependencies already installed.
    echo.
)

REM Check if .env file exists in parent directory
if not exist "..\. env" (
    echo WARNING: .env file not found in parent directory!
    echo Please copy .env.example to .env and add your Google API key
    echo.
    pause
    exit /b 1
)

REM Create necessary directories
if not exist "..\uploads\" mkdir ..\uploads
if not exist "..\data\" mkdir ..\data

REM Start the backend
echo Starting Meeting Summarizer Backend...
echo.
echo The API will be available at: http://localhost:5000
echo The frontend will be served at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
