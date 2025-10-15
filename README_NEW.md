# 🎙️ Meeting Summarizer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An AI-powered application that transcribes meeting audio files and generates action-oriented summaries with key decisions and action items.

> **Transform your meeting recordings into actionable insights in minutes!**

---

## 📁 Project Structure

```
meeting-summarizer/
│
├── 📂 backend/                    # Backend API Server
│   ├── app.py                    # Main Flask application
│   ├── config.py                 # Configuration
│   ├── requirements.txt          # Python dependencies
│   ├── services/                 # Business logic
│   │   ├── transcription_service.py  # Whisper AI
│   │   └── summarization_service.py  # Gemini AI
│   └── README.md                 # Backend documentation
│
├── 📂 frontend/                   # Frontend Web Interface
│   ├── index.html                # Web UI (HTML+CSS+JS)
│   └── README.md                 # Frontend documentation
│
├── 📂 uploads/                    # Uploaded audio files (auto-created)
├── 📂 data/                       # Processed meeting data (auto-created)
│
├── 📂 examples/                   # Example scripts
│   ├── test_api.py               # API testing tool
│   └── sample_audio.md           # Sample audio guide
│
├── 📚 Documentation/
│   ├── README.md                 # This file
│   ├── GET_STARTED.md            # Getting started guide
│   ├── QUICKSTART.md             # Quick setup
│   ├── API_DOCUMENTATION.md      # Complete API reference
│   ├── PROJECT_SUMMARY.md        # Project overview
│   └── DEMO_SCRIPT.md            # Demo video guide
│
├── .env                          # Environment variables (API key)
├── .env.example                  # Example environment file
├── .gitignore                    # Git ignore rules
│
└── Scripts/
    ├── start_backend.bat         # Windows backend startup
    ├── start_backend.sh          # macOS/Linux backend startup
    └── setup.py                  # Automated setup script
```

---

## 🚀 Quick Start

### Method 1: Using Startup Script (Easiest)

**Windows:**
```bash
start_backend.bat
```

**macOS/Linux:**
```bash
chmod +x start_backend.sh
./start_backend.sh
```

Then open your browser: **http://localhost:5000**

### Method 2: Manual Setup

#### Step 1: Install Backend

```bash
cd backend
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

#### Step 2: Configure API Key

The `.env` file is already created with your API key:
```
GOOGLE_API_KEY=AIzaSyAzZ78_NTX5bYHF3q1Ya6jnWleD1brB2rQ
```

#### Step 3: Run Backend

```bash
cd backend
python app.py
```

#### Step 4: Access Application

Open: **http://localhost:5000**

The backend serves both the API and the frontend!

---

## 📋 Features

### Backend (API Server)
- ✅ **Flask REST API** with 7 endpoints
- ✅ **OpenAI Whisper** for transcription
- ✅ **Google Gemini AI** for summarization  
- ✅ **File upload handling**
- ✅ **Data persistence** (JSON storage)
- ✅ **CORS enabled** for API access

### Frontend (Web Interface)
- ✅ **Drag & drop** file upload
- ✅ **Real-time** processing status
- ✅ **Beautiful UI** with modern design
- ✅ **Responsive** layout
- ✅ **Results display** (transcript, summary, decisions, actions)

---

## 🎯 How It Works

```
1. Frontend: User uploads audio file
   ↓
2. Backend: Saves file & returns meeting_id
   ↓
3. Backend: Transcribes with Whisper AI
   ↓
4. Backend: Summarizes with Gemini AI
   ↓
5. Frontend: Displays complete results
```

---

## 📖 Usage

### Web Interface

1. **Start the backend:**
   ```bash
   cd backend
   python app.py
   ```

2. **Open browser:**
   ```
   http://localhost:5000
   ```

3. **Upload audio file** (drag & drop or browse)

4. **Click "Process Meeting"**

5. **View results:**
   - Full transcript with timestamps
   - AI-generated summary
   - Key decisions made
   - Action items identified

### API Usage

```python
import requests

# Upload audio
files = {'audio': open('meeting.mp3', 'rb')}
response = requests.post('http://localhost:5000/api/upload', files=files)
meeting_id = response.json()['meeting_id']

# Process (transcribe + summarize)
response = requests.post(f'http://localhost:5000/api/process/{meeting_id}')
result = response.json()

print(result['summary'])
print(result['key_decisions'])
print(result['action_items'])
```

### Command Line

```bash
# Using CLI tool
python cli_tool.py meeting.mp3

# Using API test script
python examples/test_api.py meeting.mp3
```

---

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve frontend |
| `/api/health` | GET | Health check |
| `/api/upload` | POST | Upload audio file |
| `/api/transcribe/<id>` | POST | Transcribe audio |
| `/api/summarize/<id>` | POST | Generate summary |
| `/api/process/<id>` | POST | Transcribe + summarize |
| `/api/meetings` | GET | List all meetings |
| `/api/meetings/<id>` | GET | Get meeting details |

**Complete API documentation:** See `API_DOCUMENTATION.md`

---

## 🔧 Technical Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **OpenAI Whisper** - Speech-to-text
- **Google Gemini AI** - Summarization
- **Flask-CORS** - CORS support

### Frontend
- **HTML5** - Structure
- **CSS3** - Modern styling
- **Vanilla JavaScript** - No frameworks!
- **Fetch API** - HTTP requests

---

## 📦 Installation Details

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Google API key for Gemini AI

### Dependencies

The backend includes all necessary dependencies in `backend/requirements.txt`:
- flask==3.0.0
- flask-cors==4.0.0
- openai-whisper==20231117
- google-generativeai==0.3.2
- python-dotenv==1.0.0
- And more...

**Installation time:** 5-10 minutes (downloads AI models)

---

## 🎬 Creating a Demo

1. **Start the application:**
   ```bash
   cd backend
   python app.py
   ```

2. **Record demo video** showing:
   - File upload process
   - Processing progress
   - Results display (transcript, summary, decisions, actions)

3. **Duration:** 3-4 minutes

**Detailed demo guide:** See `DEMO_SCRIPT.md`

---

## 🐛 Troubleshooting

### "Module not found" errors
```bash
cd backend
pip install -r requirements.txt
```

### "Port already in use"
Edit `.env` file:
```
PORT=5001
```

### "Google API key is required"
- Check `.env` file exists in root directory
- Verify `GOOGLE_API_KEY` is set correctly

### Slow first run
- Normal! Whisper downloads models (~150MB) on first use
- Subsequent runs are much faster

**More help:** See `GET_STARTED.md` troubleshooting section

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **GET_STARTED.md** | Complete getting started guide |
| **QUICKSTART.md** | 5-minute quick setup |
| **API_DOCUMENTATION.md** | Full API reference |
| **PROJECT_SUMMARY.md** | Project overview & architecture |
| **backend/README.md** | Backend-specific documentation |
| **frontend/README.md** | Frontend-specific documentation |
| **DEMO_SCRIPT.md** | Demo video creation guide |

---

## ✅ Project Requirements Met

- ✅ **ASR Integration:** OpenAI Whisper
- ✅ **LLM Integration:** Google Gemini AI
- ✅ **Backend:** Flask REST API
- ✅ **Frontend:** Web interface for upload & viewing
- ✅ **Data Storage:** JSON-based persistence
- ✅ **Summarization:** Key decisions & action items
- ✅ **Documentation:** Comprehensive guides
- ✅ **Demo Ready:** Complete working application

---

## 🎯 Use Cases

- Corporate meeting minutes
- Interview transcription
- Lecture summarization
- Podcast analysis
- Legal depositions
- Medical consultations

---

## 🔒 Security

- API key stored in `.env` (not in git)
- File type validation on uploads
- File size limits enforced
- CORS configured for production
- Input sanitization

---

## 🚀 Deployment

### Local Development
```bash
cd backend
python app.py
```

### Production (with Gunicorn)
```bash
cd backend
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📝 License

This project is for educational and demonstration purposes.

---

## 🤝 Support

- **Documentation:** See docs folder
- **Issues:** Check troubleshooting sections
- **Examples:** See `examples/` folder

---

## 🎓 Learning Outcomes

This project demonstrates:
- Full-stack development (Backend + Frontend)
- AI/ML integration (ASR + LLM)
- REST API design
- Modern web development
- Clean code architecture
- Comprehensive documentation

---

## 🎉 Ready to Use!

**Start the backend:**
```bash
cd backend
python app.py
```

**Open your browser:**
```
http://localhost:5000
```

**Upload an audio file and see the magic happen!** ✨

---

*Built with ❤️ for intelligent meeting management*
