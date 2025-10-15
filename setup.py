"""
Initial setup script for Meeting Summarizer
Run this once to set up your development environment
"""
import os
import sys
import subprocess

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")

def check_python_version():
    """Check if Python version is compatible"""
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Python 3.8 or higher is required")
        return False
    
    print("✓ Python version is compatible")
    return True

def create_virtual_environment():
    """Create a virtual environment"""
    print_header("Creating Virtual Environment")
    
    if os.path.exists("venv"):
        print("Virtual environment already exists")
        return True
    
    try:
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✓ Virtual environment created successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating virtual environment: {e}")
        return False

def get_pip_command():
    """Get the correct pip command based on OS"""
    if os.name == 'nt':  # Windows
        return os.path.join("venv", "Scripts", "pip.exe")
    else:  # macOS/Linux
        return os.path.join("venv", "bin", "pip")

def install_dependencies():
    """Install required packages"""
    print_header("Installing Dependencies")
    
    pip_cmd = get_pip_command()
    
    if not os.path.exists(pip_cmd):
        print("❌ Error: Virtual environment not found. Please create it first.")
        return False
    
    try:
        print("Upgrading pip...")
        subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)
        
        print("\nInstalling required packages...")
        print("This may take 5-10 minutes (downloading AI models)...")
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def setup_environment_file():
    """Set up the .env file"""
    print_header("Setting Up Environment File")
    
    if os.path.exists(".env"):
        print(".env file already exists")
        
        # Check if API key is set
        with open(".env", "r") as f:
            content = f.read()
            if "AIzaSyAzZ78_NTX5bYHF3q1Ya6jnWleD1brB2rQ" in content:
                print("✓ Google API key is already configured")
                return True
            elif "your_google_api_key_here" in content or "GOOGLE_API_KEY=" not in content:
                print("⚠ Warning: Please update your Google API key in .env file")
                return True
    else:
        print(".env file not found. It should already exist with your API key.")
        print("⚠ Warning: Please make sure .env file has your Google API key")
    
    return True

def create_directories():
    """Create necessary directories"""
    print_header("Creating Directories")
    
    directories = ["uploads", "data"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Created {directory}/ directory")
        else:
            print(f"{directory}/ directory already exists")
    
    return True

def print_next_steps():
    """Print instructions for next steps"""
    print_header("Setup Complete! 🎉")
    
    print("Next steps:")
    print()
    print("1. Activate the virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # macOS/Linux
        print("   source venv/bin/activate")
    print()
    print("2. Verify your Google API key in .env file")
    print()
    print("3. Start the application:")
    print("   python app.py")
    print()
    print("4. Open your browser:")
    print("   http://localhost:5000")
    print()
    print("For more information, see:")
    print("  - README.md - Complete documentation")
    print("  - QUICKSTART.md - Quick start guide")
    print("  - API_DOCUMENTATION.md - API reference")
    print()

def main():
    """Main setup function"""
    print_header("Meeting Summarizer - Initial Setup")
    
    print("This script will:")
    print("  1. Check Python version")
    print("  2. Create virtual environment")
    print("  3. Install dependencies")
    print("  4. Set up environment file")
    print("  5. Create necessary directories")
    print()
    
    input("Press Enter to continue...")
    
    # Run setup steps
    if not check_python_version():
        return
    
    if not create_virtual_environment():
        return
    
    if not install_dependencies():
        return
    
    if not setup_environment_file():
        return
    
    if not create_directories():
        return
    
    print_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
