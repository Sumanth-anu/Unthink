# API Documentation

## Meeting Summarizer REST API

Base URL: `http://localhost:5000`

---

## Endpoints

### 1. Health Check

Check if the API is running.

**Endpoint:** `GET /api/health`

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T14:30:22.123456"
}
```

---

### 2. Upload Audio File

Upload a meeting audio file for processing.

**Endpoint:** `POST /api/upload`

**Content-Type:** `multipart/form-data`

**Parameters:**
- `audio` (file, required): Audio file to upload

**Supported Formats:**
- WAV
- MP3
- M4A
- FLAC
- OGG
- WEBM

**Max File Size:** 100 MB (configurable)

**Example Request (curl):**
```bash
curl -X POST http://localhost:5000/api/upload \
  -F "audio=@meeting.mp3"
```

**Example Request (Python):**
```python
import requests

with open('meeting.mp3', 'rb') as f:
    files = {'audio': f}
    response = requests.post('http://localhost:5000/api/upload', files=files)
    print(response.json())
```

**Success Response (200):**
```json
{
  "meeting_id": "20240115_143022",
  "filename": "meeting.mp3",
  "message": "File uploaded successfully"
}
```

**Error Response (400):**
```json
{
  "error": "No audio file provided"
}
```

---

### 3. Transcribe Audio

Transcribe an uploaded audio file to text.

**Endpoint:** `POST /api/transcribe/{meeting_id}`

**Parameters:**
- `meeting_id` (path, required): Meeting ID from upload response

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/transcribe/20240115_143022
```

**Success Response (200):**
```json
{
  "meeting_id": "20240115_143022",
  "transcript": "Welcome everyone to today's meeting...",
  "language": "en",
  "message": "Transcription completed successfully"
}
```

**Error Response (404):**
```json
{
  "error": "Audio file not found"
}
```

---

### 4. Generate Summary

Generate a summary from a transcribed meeting.

**Endpoint:** `POST /api/summarize/{meeting_id}`

**Parameters:**
- `meeting_id` (path, required): Meeting ID with existing transcript

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/summarize/20240115_143022
```

**Success Response (200):**
```json
{
  "meeting_id": "20240115_143022",
  "summary": "The meeting focused on Q1 planning...",
  "key_decisions": [
    "Implement two-factor authentication",
    "Postpone mobile redesign to Q2"
  ],
  "action_items": [
    "Create technical spec by Jan 20",
    "Review authentication vendors by Jan 25"
  ],
  "message": "Summary generated successfully"
}
```

**Error Response (404):**
```json
{
  "error": "Transcript not found. Please transcribe first."
}
```

---

### 5. Process Meeting (All-in-One)

Upload, transcribe, and summarize in a single request.

**Endpoint:** `POST /api/process/{meeting_id}`

**Parameters:**
- `meeting_id` (path, required): Meeting ID from upload response

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/process/20240115_143022
```

**Success Response (200):**
```json
{
  "meeting_id": "20240115_143022",
  "transcript": "Full meeting transcript...",
  "language": "en",
  "summary": "Meeting summary...",
  "key_decisions": [
    "Decision 1",
    "Decision 2"
  ],
  "action_items": [
    "Action 1",
    "Action 2"
  ],
  "message": "Meeting processed successfully"
}
```

---

### 6. List All Meetings

Get a list of all processed meetings.

**Endpoint:** `GET /api/meetings`

**Example Request:**
```bash
curl http://localhost:5000/api/meetings
```

**Success Response (200):**
```json
{
  "meetings": [
    {
      "meeting_id": "20240115_143022",
      "timestamp": "2024-01-15T14:30:22.123456",
      "has_transcript": true,
      "has_summary": true
    },
    {
      "meeting_id": "20240114_100530",
      "timestamp": "2024-01-14T10:05:30.654321",
      "has_transcript": true,
      "has_summary": false
    }
  ]
}
```

---

### 7. Get Meeting Details

Retrieve complete details of a specific meeting.

**Endpoint:** `GET /api/meetings/{meeting_id}`

**Parameters:**
- `meeting_id` (path, required): Meeting identifier

**Example Request:**
```bash
curl http://localhost:5000/api/meetings/20240115_143022
```

**Success Response (200):**
```json
{
  "meeting_id": "20240115_143022",
  "timestamp": "2024-01-15T14:30:22.123456",
  "transcript": "Full transcript...",
  "segments": [
    {
      "start": 0.0,
      "end": 15.5,
      "text": "Welcome everyone..."
    }
  ],
  "language": "en",
  "summary": "Meeting summary...",
  "key_decisions": ["Decision 1", "Decision 2"],
  "action_items": ["Action 1", "Action 2"],
  "summary_timestamp": "2024-01-15T14:32:45.789012"
}
```

**Error Response (404):**
```json
{
  "error": "Meeting not found"
}
```

---

## Workflow Examples

### Complete Workflow (Separate Steps)

```python
import requests
import time

BASE_URL = "http://localhost:5000"

# Step 1: Upload
with open('meeting.mp3', 'rb') as f:
    files = {'audio': f}
    response = requests.post(f"{BASE_URL}/api/upload", files=files)
    meeting_id = response.json()['meeting_id']
    print(f"Uploaded: {meeting_id}")

# Step 2: Transcribe
response = requests.post(f"{BASE_URL}/api/transcribe/{meeting_id}")
print(f"Transcribed: {response.json()['transcript'][:100]}...")

# Step 3: Summarize
response = requests.post(f"{BASE_URL}/api/summarize/{meeting_id}")
summary = response.json()
print(f"Summary: {summary['summary']}")
print(f"Key Decisions: {summary['key_decisions']}")
print(f"Action Items: {summary['action_items']}")
```

### Complete Workflow (One-Step)

```python
import requests

BASE_URL = "http://localhost:5000"

# Step 1: Upload
with open('meeting.mp3', 'rb') as f:
    files = {'audio': f}
    response = requests.post(f"{BASE_URL}/api/upload", files=files)
    meeting_id = response.json()['meeting_id']

# Step 2: Process (transcribe + summarize)
response = requests.post(f"{BASE_URL}/api/process/{meeting_id}")
result = response.json()

print(f"Transcript: {result['transcript'][:100]}...")
print(f"Summary: {result['summary']}")
print(f"Decisions: {result['key_decisions']}")
print(f"Actions: {result['action_items']}")
```

---

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request (invalid input)
- `404` - Not Found (resource doesn't exist)
- `500` - Internal Server Error

Error responses include a descriptive message:
```json
{
  "error": "Description of what went wrong"
}
```

---

## Rate Limiting

Currently, no rate limiting is implemented. For production use, consider:
- Adding rate limiting middleware
- Implementing authentication
- Using API keys for access control

---

## Notes

1. **Processing Time**: Transcription and summarization may take 1-5 minutes depending on audio length
2. **File Storage**: Uploaded files are stored in the `uploads/` directory
3. **Data Persistence**: Meeting data is stored as JSON files in the `data/` directory
4. **Concurrent Requests**: The API can handle multiple requests, but processing is sequential per meeting
5. **API Key**: Google API key must be configured in `.env` file

---

## Testing

Use the provided test script:
```bash
python examples/test_api.py path/to/audio.mp3
```

Or use curl for individual endpoints:
```bash
# Health check
curl http://localhost:5000/api/health

# List meetings
curl http://localhost:5000/api/meetings
```
