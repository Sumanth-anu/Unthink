# Frontend - Meeting Summarizer UI

This is the **frontend interface** for the Meeting Summarizer application.

## 🎨 What's Inside

A beautiful, modern, single-page web application with:
- **Drag & Drop** file upload
- **Real-time** processing status
- **Beautiful UI** for displaying results
- **Responsive design** that works on all devices

## 📂 Structure

```
frontend/
└── index.html    # Complete single-page application
                  # (HTML + CSS + JavaScript)
```

## 🚀 Running the Frontend

### Option 1: Via Backend Server (Recommended)

The backend automatically serves the frontend:

1. Start the backend server (from backend folder):
   ```bash
   cd ../backend
   python app.py
   ```

2. Open your browser:
   ```
   http://localhost:5000
   ```

The backend serves `index.html` at the root path!

### Option 2: Standalone (Development)

Open the file directly in your browser:
```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

**Note:** When running standalone, update the API URL in `index.html`:
```javascript
const BASE_URL = "http://localhost:5000";  // Update if needed
```

## ✨ Features

### 1. File Upload
- **Drag & Drop** - Intuitive file upload
- **Browse** - Traditional file picker
- **Validation** - Checks file types and size
- **Feedback** - Shows selected file info

### 2. Processing View
- **Progress Indicators** - 4-step process visualization
- **Loading Animation** - Shows processing status
- **Error Handling** - Clear error messages
- **Status Updates** - Real-time feedback

### 3. Results Display
- **📝 Transcript** - Full meeting transcript with scroll
- **📋 Summary** - AI-generated summary
- **🎯 Key Decisions** - Extracted decisions list
- **✅ Action Items** - Identified action items
- **Meeting Info** - ID and language badges

### 4. User Experience
- **Smooth Scrolling** - Auto-scroll to results
- **Reset Function** - Process another meeting
- **Responsive** - Works on mobile & desktop
- **Modern Design** - Purple gradient theme

## 🎨 Design Features

- **Color Scheme:** Purple gradient (#667eea to #764ba2)
- **Typography:** Segoe UI font family
- **Animations:** Smooth transitions and hover effects
- **Icons:** Emoji-based icons for clarity
- **Layout:** Card-based, centered design

## 🔧 Customization

### Change API Endpoint

Edit the `BASE_URL` in `index.html`:
```javascript
const BASE_URL = "http://your-backend-url:5000";
```

### Change Colors

Update the CSS variables in `<style>` section:
```css
background: linear-gradient(135deg, #your-color-1, #your-color-2);
```

### Add Features

The JavaScript is modular and well-commented. Key functions:
- `handleFile()` - File upload handling
- `processAudio()` - Complete processing workflow
- `displayResults()` - Results rendering
- `resetApp()` - Reset functionality

## 📱 Supported Browsers

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Edge
- ✅ Safari
- ✅ Opera

## 📋 Supported Audio Formats

- WAV
- MP3
- M4A
- FLAC
- OGG
- WEBM

Max file size: **100MB**

## 🎯 How It Works

```
1. User uploads audio file
   ↓
2. File sent to /api/upload
   ↓
3. Backend returns meeting_id
   ↓
4. Frontend calls /api/process/{meeting_id}
   ↓
5. Backend transcribes + summarizes
   ↓
6. Frontend displays results
```

## 🐛 Troubleshooting

**CORS errors:**
- Make sure backend is running
- Check backend CORS configuration
- Verify API URL is correct

**Upload fails:**
- Check file format (must be audio)
- Verify file size (< 100MB)
- Ensure backend is accessible

**No results showing:**
- Open browser console (F12)
- Check for JavaScript errors
- Verify API responses

## 📝 Technical Details

### Technology Stack
- **HTML5** - Structure
- **CSS3** - Styling (no frameworks!)
- **Vanilla JavaScript** - Functionality (no jQuery!)
- **Fetch API** - HTTP requests
- **FormData API** - File uploads

### Browser APIs Used
- Fetch API for HTTP requests
- FormData for file uploads
- Drag and Drop API
- DOM manipulation
- Smooth scroll behavior

## 🎨 Future Enhancements

Potential improvements:
- [ ] React/Vue.js version
- [ ] Dark mode toggle
- [ ] Export results to PDF
- [ ] Real-time transcription progress
- [ ] Audio player with transcript sync
- [ ] Multi-language UI
- [ ] User authentication
- [ ] Meeting history view

## 📚 Code Structure

The `index.html` file contains:

1. **HTML Structure** - Semantic markup
2. **CSS Styles** - Embedded in `<style>` tag
3. **JavaScript** - Embedded in `<script>` tag

All-in-one file for easy deployment!

---

**Frontend is ready to use! 🎨**

Open `http://localhost:5000` after starting the backend!
