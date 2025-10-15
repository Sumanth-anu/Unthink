# Backend - Meeting Summarizer API

This is the **backend server** for the Meeting Summarizer application.

## 🔧 What's Inside

- **Flask REST API** - Complete backend server
- **OpenAI Whisper** - Audio transcription service
- **Google Gemini AI** - Meeting summarization service
- **Data Storage** - JSON-based meeting data storage

## 📂 Structure

```
backend/
├── app.py                      # Main Flask application
├── config.py                   # Configuration management
├── requirements.txt            # Python dependencies
└── services/
    ├── __init__.py
    ├── transcription_service.py   # Whisper transcription
    └── summarization_service.py   # Gemini summarization
```

## 🚀 Running the Backend

### Prerequisites
- Python 3.8+
- Google API key (already in parent `.env` file)

### Installation

1. **Navigate to backend folder:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   python app.py
   ```

The backend will start on **http://localhost:5000**

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/upload` | POST | Upload audio file |
| `/api/transcribe/<id>` | POST | Transcribe audio |
| `/api/summarize/<id>` | POST | Generate summary |
| `/api/process/<id>` | POST | Transcribe + summarize |
| `/api/meetings` | GET | List all meetings |
| `/api/meetings/<id>` | GET | Get meeting details |

## 🔑 Environment Variables

The backend reads from the `.env` file in the **parent directory**:

```
GOOGLE_API_KEY=your_api_key_here
FLASK_DEBUG=True
PORT=5000
```

## 🧪 Testing

```bash
# Test health endpoint
curl http://localhost:5000/api/health

# Upload audio
curl -X POST http://localhost:5000/api/upload -F "audio=@test.mp3"
```

## 📦 Dependencies

- **Flask** - Web framework
- **Flask-CORS** - CORS support
- **OpenAI Whisper** - Speech-to-text
- **Google Generative AI** - Summarization
- **python-dotenv** - Environment management

See `requirements.txt` for complete list.

## 🔒 CORS Configuration

The backend is configured to accept requests from any origin during development. For production, update the CORS settings in `app.py`:

```python
CORS(app, resources={r"/api/*": {"origins": "https://your-frontend-domain.com"}})
```

## 📝 Notes

- Audio files are stored in `../uploads/` (parent directory)
- Meeting data is stored in `../data/` (parent directory)
- The backend serves the frontend at the root path `/`
- All API endpoints are prefixed with `/api/`

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Change port in parent .env file
PORT=5001
```

**Module not found:**
```bash
pip install -r requirements.txt
```

**API key error:**
- Check that `.env` exists in parent directory
- Verify `GOOGLE_API_KEY` is set

## 📚 Documentation

For complete API documentation, see `../API_DOCUMENTATION.md` in the parent directory.

---

**Backend is ready to serve! 🚀**
