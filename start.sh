#!/bin/bash
# Startup script for Meeting Summarizer on macOS/Linux

echo "========================================"
echo "Meeting Summarizer - Startup Script"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Check if requirements are installed
echo "Checking dependencies..."
if ! pip show flask > /dev/null 2>&1; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo ""
else
    echo "Dependencies already installed."
    echo ""
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "WARNING: .env file not found!"
    echo "Please copy .env.example to .env and add your Google API key"
    echo ""
    exit 1
fi

# Create necessary directories
mkdir -p uploads
mkdir -p data

# Start the application
echo "Starting Meeting Summarizer..."
echo ""
echo "The application will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""
python app.py
