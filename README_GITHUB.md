# 🎙️ Meeting Summarizer - AI-Powered Meeting Analysis

> Transform your meeting recordings into actionable insights using AI

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![OpenAI Whisper](https://img.shields.io/badge/Whisper-Latest-orange.svg)
![Google Gemini](https://img.shields.io/badge/Gemini-2.5--flash-purple.svg)

---

## 📋 Overview

**Meeting Summarizer** is an AI-powered web application that automatically transcribes and summarizes meeting recordings. It uses state-of-the-art AI models to extract key decisions, action items, and provide comprehensive meeting summaries.

### ✨ Key Features

- 🎵 **Audio Transcription** - Powered by OpenAI Whisper AI
- 🤖 **AI Summarization** - Using Google Gemini 2.5 Flash
- ✅ **Key Decisions Extraction** - Automatically identifies important decisions
- 🎯 **Action Items Detection** - Extracts tasks and assignments
- 🎨 **Beautiful Modern UI** - Animated, responsive interface
- 📊 **Real-time Processing** - Watch progress with animated indicators
- 💾 **Data Persistence** - Save and retrieve meeting results

---

## 🖼️ Screenshots

### Main Interface
Beautiful dark gradient background with animated elements and modern design.

### Processing View
Multi-step progress indicator showing transcription and summarization stages.

### Results Display
Clean, organized display of transcript, summary, key decisions, and action items.

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **FFmpeg** (for audio processing)
- **Google Gemini API Key** ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Sumanth-anu/Unthink.git
cd Unthink
```

2. **Set up Python virtual environment:**
```bash
cd backend
python -m venv venv
```

3. **Activate virtual environment:**
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Install FFmpeg:**
- **Windows**: Download from [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

6. **Configure API Key:**
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

7. **Run the application:**
```bash
python app.py
```

8. **Open your browser:**
Navigate to `http://localhost:5000`

---

## 📖 How to Use

### Step 1: Upload Audio File
- Drag and drop your meeting recording (MP3, WAV, M4A, FLAC, OGG, WEBM)
- Or click "Browse Files" to select a file

### Step 2: Process Meeting
- Click the "Process Meeting" button
- Wait 2-3 minutes for processing (animated spinner shows progress)

### Step 3: View Results
You'll receive:
- **📝 Complete Transcript** - Full text of the meeting
- **📊 AI Summary** - 2-3 paragraph overview
- **✅ Key Decisions** - Important decisions made
- **🎯 Action Items** - Tasks and assignments

---

## 🏗️ Architecture

### Backend (Flask API)
```
backend/
├── app.py                          # Main Flask application
├── config.py                       # Configuration management
├── requirements.txt                # Python dependencies
└── services/
    ├── transcription_service.py    # Whisper AI integration
    └── summarization_service.py    # Gemini AI integration
```

### Frontend (Pure HTML/CSS/JS)
```
frontend/
└── index.html                      # Single-page application
```

### Tech Stack

**Backend:**
- Flask 3.0 (Web framework)
- OpenAI Whisper (Speech-to-text)
- Google Gemini AI (Text summarization)
- Python-dotenv (Environment management)

**Frontend:**
- HTML5, CSS3, Vanilla JavaScript
- Modern animations and transitions
- Responsive design

---

## 🔧 Configuration

### Supported Audio Formats
- MP3
- WAV
- M4A
- FLAC
- OGG
- WEBM

### Whisper Model Sizes
Default: `base` (fast, good accuracy)

Available options:
- `tiny` - Fastest, lowest accuracy
- `base` - Good balance (default)
- `small` - Better accuracy
- `medium` - High accuracy
- `large` - Best accuracy (slowest)

### API Endpoints

- `GET /api/health` - Health check
- `POST /api/upload` - Upload audio file
- `POST /api/process/<meeting_id>` - Process meeting
- `GET /api/meetings` - List all meetings
- `GET /api/meetings/<meeting_id>` - Get specific meeting

---

## 📊 Performance

**Processing Time** (for base model):
- 30-second audio: ~1-2 minutes
- 1-minute audio: ~2-3 minutes
- 5-minute audio: ~5-8 minutes

**First Run**: Additional 2-3 minutes to download Whisper model (~150MB)

---

## 🎨 Features Showcase

### Beautiful Animations
- ✨ Floating sparkles around cards
- 🌈 Flowing gradient text effects
- 💫 Animated background grid
- 🎯 Bouncing upload icon
- ⚡ Button shimmer effects
- 📊 Staggered slide-in animations

### User Experience
- Drag & drop file upload
- Real-time progress tracking
- Responsive design
- Error handling with helpful messages
- Beautiful loading animations

---

## 📁 Project Structure

```
meeting-summarizer/
├── backend/                    # Backend Flask application
│   ├── app.py                 # Main API server
│   ├── config.py              # Configuration
│   ├── requirements.txt       # Dependencies
│   └── services/              # AI services
│       ├── transcription_service.py
│       └── summarization_service.py
├── frontend/                   # Frontend web app
│   └── index.html             # Main UI
├── uploads/                    # Uploaded audio files (gitignored)
├── data/                       # Processed results (gitignored)
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## 🔒 Security

- API keys stored in `.env` (not committed to Git)
- File upload validation
- CORS protection
- Secure file handling

---

## 🐛 Troubleshooting

### "Processing Failed" Error

**Cause**: FFmpeg not installed or not in PATH

**Solution**:
1. Install FFmpeg (see Installation section)
2. Add FFmpeg to your system PATH
3. Restart the application

### "Invalid API Key" Error

**Cause**: Google Gemini API key not configured

**Solution**:
1. Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add to `.env` file: `GOOGLE_API_KEY=your_key_here`
3. Restart the application

### Slow Processing

**Cause**: Using large Whisper model or long audio file

**Solution**:
- Use `base` or `small` model for faster processing
- Ensure audio file is under 10 minutes
- Check CPU usage

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Sumanth Naik**
- GitHub: [@Sumanth-anu](https://github.com/Sumanth-anu)
- Repository: [Unthink](https://github.com/Sumanth-anu/Unthink)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

## 📞 Support

For support, create an issue in the [GitHub repository](https://github.com/Sumanth-anu/Unthink/issues).

---

## 🔮 Future Enhancements

- [ ] Support for video files
- [ ] Multiple language support
- [ ] Speaker diarization (identify who said what)
- [ ] Export to PDF/DOCX
- [ ] Integration with calendar apps
- [ ] Real-time transcription
- [ ] Team collaboration features
- [ ] Meeting templates
- [ ] Custom prompts for summarization

---

<div align="center">

**Built with ❤️ using AI**

[Report Bug](https://github.com/Sumanth-anu/Unthink/issues) · [Request Feature](https://github.com/Sumanth-anu/Unthink/issues)

</div>
