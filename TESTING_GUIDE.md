# 🧪 Testing Guide - Meeting Summarizer

## ✅ Server Status
Your backend is running on: **http://localhost:5000**

---

## 📤 How to Test the Application

### **Step 1: Get a Test Audio File**

You need an audio file with speech. Here are your options:

#### **Option A: Use Your Phone** (EASIEST)
1. Record a short voice memo on your phone (30 seconds - 2 minutes)
2. Say something like:
   ```
   "Hello team, this is our project meeting. 
   We need to discuss three items today.
   First, the product launch - John will handle marketing.
   Second, budget approval - we decided to increase it by 20%.
   Third action item - Sarah to complete the report by Friday.
   Thank you everyone."
   ```
3. Transfer the audio file to your computer
4. Supported formats: MP3, WAV, M4A

#### **Option B: Download a Sample**
- Go to: https://www.kozco.com/tech/audiosample.html
- Download any sample audio file
- Or use: https://www2.cs.uic.edu/~i101/SoundFiles/

#### **Option C: Use Online TTS**
1. Go to: https://ttsmp3.com/
2. Paste this text:
   ```
   Hello everyone, this is our quarterly meeting. First agenda is the product launch. 
   John will handle marketing. Sarah will manage development. 
   Key decision: Launch in December. 
   Action item: John to prepare materials by Friday.
   ```
3. Click "Convert to MP3"
4. Download the MP3 file

---

### **Step 2: Upload & Process**

1. **Open the application**: http://localhost:5000
2. **Upload your audio**:
   - Drag and drop the file into the upload area, OR
   - Click "Browse Files" and select your audio file
3. **Click "Process Meeting"** button
4. **Wait** (2-3 minutes for a 1-minute audio)
   - You'll see an animated spinner
   - First: Whisper transcribes the audio
   - Then: Gemini AI generates the summary

---

### **Step 3: Expected Output**

You should see 4 beautiful animated cards with:

#### **1. 📝 Transcript**
Full text of what was spoken in the audio

#### **2. 📊 Meeting Summary**  
2-3 paragraph AI-generated overview of the meeting

#### **3. ✅ Key Decisions**
Bullet points of important decisions made

#### **4. 🎯 Action Items**
List of tasks and assignments mentioned

---

## 🔍 Troubleshooting

### **If Upload Fails:**
- Check file format (must be: WAV, MP3, M4A, FLAC, OGG, WEBM)
- Check file size (should be under 100MB)
- Make sure the file actually contains speech/audio

### **If Processing Fails:**
Check the PowerShell terminal for error messages. Common issues:

1. **FFmpeg Error**: Make sure FFmpeg is in PATH
2. **Gemini API Error**: Check your API key in `.env` file
3. **No Speech Detected**: Audio file might be silent or corrupted

### **To See Server Logs:**
Look at the PowerShell window where the server is running. You'll see:
```
Starting transcription for [meeting_id]...
Loading Whisper base model...
Transcribing audio file: [filepath]
Generating summary for [meeting_id]...
```

---

## 📂 Test File Locations

After upload, files are saved in:
- **Uploaded Audio**: `meeting-summarizer/uploads/`
- **Results JSON**: `meeting-summarizer/data/`

You can check these folders to verify files are being saved.

---

## 🎯 Quick Test

**Minimum test audio (record on your phone):**
```
"Hello, this is a test meeting. 
We have three action items.
First, John will review the budget.
Second, Sarah will prepare the presentation.
Third, we all need to attend the workshop next Monday.
Meeting adjourned."
```

Save as MP3, upload, and you should get:
- ✅ Transcript of the speech
- ✅ Summary about budget review and workshop
- ✅ Key decision to attend workshop
- ✅ Action items for John and Sarah

---

## 🆘 Still Having Issues?

1. **Check if server is running**: Open http://localhost:5000 in browser
2. **Check FFmpeg**: Run `C:\Users\Sumanth Naik\OneDrive\Desktop\Unthinkable\meeting-summarizer\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe -version` in PowerShell
3. **Check API key**: Open `.env` file and verify `GOOGLE_API_KEY` is set
4. **Try a different audio file**: Maybe your file is corrupted

---

## ✨ Expected Behavior

**Timeline for 1-minute audio:**
- 0:00 - Upload complete (instant)
- 0:00-2:30 - Transcription with Whisper (animated spinner)
- 2:30-2:45 - AI Summary with Gemini (still spinning)
- 2:45 - Results appear with beautiful slide-in animations!

Good luck testing! 🚀
