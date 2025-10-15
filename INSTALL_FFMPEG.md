# 🎬 Install FFmpeg (Required for Audio Processing)

## ❗ Error You're Seeing:
`FileNotFoundError: [WinError 2] The system cannot find the file specified`

This happens because **Whisper requires FFmpeg** to process audio files on Windows.

---

## ✅ **Quick Fix - Install FFmpeg:**

### **Option 1: Download FFmpeg (Recommended for Windows)**

1. **Download FFmpeg:**
   - Go to: https://www.gyan.dev/ffmpeg/builds/
   - Download: `ffmpeg-release-essentials.zip` (the first download link)

2. **Extract the ZIP file:**
   - Extract to: `C:\ffmpeg`
   - You should have: `C:\ffmpeg\bin\ffmpeg.exe`

3. **Add to System PATH:**
   - Press `Windows + R`
   - Type: `sysdm.cpl` and press Enter
   - Go to "Advanced" tab → Click "Environment Variables"
   - Under "System variables", find "Path" → Click "Edit"
   - Click "New" → Add: `C:\ffmpeg\bin`
   - Click "OK" on all windows

4. **Verify Installation:**
   - Open a **NEW** PowerShell window
   - Run: `ffmpeg -version`
   - You should see FFmpeg version information

5. **Restart the Backend:**
   - Stop the running server (Ctrl+C in terminal)
   - Run: `.\venv\Scripts\python.exe app.py`
   - Try uploading again!

---

### **Option 2: Using Winget (Windows Package Manager)**

```powershell
winget install --id=Gyan.FFmpeg -e
```

Then add `C:\ffmpeg\bin` to your PATH as described above.

---

### **Option 3: Using Scoop (If you have it installed)**

```powershell
scoop install ffmpeg
```

---

## 🔄 **After Installing FFmpeg:**

1. **Close and reopen** PowerShell (to refresh PATH)
2. **Verify** FFmpeg is working:
   ```powershell
   ffmpeg -version
   ```
3. **Restart the backend server**
4. **Try uploading your audio file again!**

---

## 🎯 **Quick Test:**

Once FFmpeg is installed, your Meeting Summarizer will be able to:
- ✅ Process MP3, WAV, M4A files
- ✅ Transcribe audio with Whisper
- ✅ Generate AI summaries with Gemini
- ✅ Extract key decisions and action items

---

## 📝 **Alternative: Use Pre-converted Audio**

If you can't install FFmpeg right now, you can:
1. Convert your audio to WAV format using an online converter
2. Make sure it's mono channel, 16kHz sample rate
3. Upload the WAV file

But installing FFmpeg is the best long-term solution! 🚀
