# Quick Start Guide

## Getting Started in 5 Minutes

### 1. Prerequisites Check
Before starting, ensure you have:
- ✅ Python 3.8 or higher installed
- ✅ pip (comes with Python)
- ✅ A Google API key for Gemini AI ([Get one here](https://makersuite.google.com/app/apikey))

### 2. Installation Steps

#### Step 1: Navigate to Project Directory
```bash
cd meeting-summarizer
```

#### Step 2: Create Virtual Environment (Recommended)
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- OpenAI Whisper (transcription)
- Google Generative AI (summarization)
- And other required packages

**Note:** First installation may take 5-10 minutes as it downloads AI models.

#### Step 4: Configure API Key
1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```

2. Open `.env` in a text editor and add your Google API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

#### Step 5: Run the Application
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

#### Step 6: Open in Browser
Navigate to: **http://localhost:5000**

### 3. First Test

1. **Prepare an audio file** (MP3, WAV, etc.)
   - Record a short 1-minute voice memo, OR
   - Use any audio file you have

2. **Upload the file**
   - Drag and drop onto the upload area, OR
   - Click "Browse Files" and select your file

3. **Process**
   - Click "Process Meeting"
   - Wait 1-3 minutes (depending on file length)

4. **View Results**
   - Scroll down to see transcript
   - Review AI-generated summary
   - Check key decisions and action items

## Alternative: Command Line Tool

For quick testing without the web interface:

```bash
python cli_tool.py your_audio_file.mp3
```

Results will be displayed in terminal and saved to a text file.

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### "No module named 'dotenv'"
```bash
pip install python-dotenv
```

### "Google API key is required"
- Make sure `.env` file exists
- Check that GOOGLE_API_KEY is set correctly
- No quotes needed around the API key

### Slow first run
- Normal! Whisper downloads AI models on first use (~150MB)
- Subsequent runs will be much faster

### Port already in use
Change the port in `.env`:
```
PORT=5001
```

## Next Steps

- 📖 Read the full [README.md](README.md) for detailed documentation
- 🧪 Try the API with [examples/test_api.py](examples/test_api.py)
- 🎥 Record a demo video using [DEMO_SCRIPT.md](DEMO_SCRIPT.md)

## Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed: `pip list`
3. Make sure you're in the virtual environment (should see `(venv)` in terminal)
4. Review the [README.md](README.md) troubleshooting section

---

**Ready to start?** Run `python app.py` and visit http://localhost:5000 🚀
