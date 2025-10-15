"""
Flask Backend API for Meeting Summarizer
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime
import traceback

from config import Config
from services import TranscriptionService, SummarizationService

app = Flask(__name__)
app.config.from_object(Config)
Config.init_app(app)

# Enable CORS for frontend
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize services (lazy loading)
transcription_service = None
summarization_service = None


def get_transcription_service():
    """Lazy load transcription service"""
    global transcription_service
    if transcription_service is None:
        transcription_service = TranscriptionService(model_size="base")
    return transcription_service


def get_summarization_service():
    """Lazy load summarization service"""
    global summarization_service
    if summarization_service is None:
        summarization_service = SummarizationService()
    return summarization_service


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def save_result(meeting_id: str, data: dict):
    """Save meeting result to JSON file"""
    filepath = os.path.join(app.config['DATA_FOLDER'], f"{meeting_id}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_result(meeting_id: str):
    """Load meeting result from JSON file"""
    filepath = os.path.join(app.config['DATA_FOLDER'], f"{meeting_id}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


# Serve frontend
@app.route('/')
def index():
    """Serve the frontend index.html"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')
    return send_from_directory(frontend_path, 'index.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })


@app.route('/api/upload', methods=['POST'])
def upload_audio():
    """
    Upload audio file for processing
    
    Returns:
        JSON with meeting_id for tracking
    """
    try:
        # Check if file is present
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        file = request.files['audio']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'error': f'File type not allowed. Allowed types: {", ".join(app.config["ALLOWED_EXTENSIONS"])}'
            }), 400
        
        # Generate unique meeting ID
        meeting_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = secure_filename(file.filename)
        
        # Save the uploaded file
        file_ext = filename.rsplit('.', 1)[1].lower()
        audio_filename = f"{meeting_id}.{file_ext}"
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
        file.save(audio_path)
        
        return jsonify({
            'meeting_id': meeting_id,
            'filename': filename,
            'message': 'File uploaded successfully'
        }), 200
        
    except Exception as e:
        print(f"Error uploading file: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/transcribe/<meeting_id>', methods=['POST'])
def transcribe(meeting_id):
    """
    Transcribe audio file
    
    Args:
        meeting_id: Unique meeting identifier
    
    Returns:
        JSON with transcript
    """
    try:
        # Find the audio file
        audio_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) 
                      if f.startswith(meeting_id)]
        
        if not audio_files:
            return jsonify({'error': 'Audio file not found'}), 404
        
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_files[0])
        
        # Transcribe
        print(f"Starting transcription for {meeting_id}...")
        service = get_transcription_service()
        result = service.transcribe_audio(audio_path)
        
        # Save result
        data = {
            'meeting_id': meeting_id,
            'timestamp': datetime.now().isoformat(),
            'transcript': result['transcript'],
            'segments': result['segments'],
            'language': result['language']
        }
        save_result(meeting_id, data)
        
        return jsonify({
            'meeting_id': meeting_id,
            'transcript': result['transcript'],
            'language': result['language'],
            'message': 'Transcription completed successfully'
        }), 200
        
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/summarize/<meeting_id>', methods=['POST'])
def summarize(meeting_id):
    """
    Generate summary for transcribed meeting
    
    Args:
        meeting_id: Unique meeting identifier
    
    Returns:
        JSON with summary, key decisions, and action items
    """
    try:
        # Load the transcription result
        data = load_result(meeting_id)
        
        if not data or 'transcript' not in data:
            return jsonify({'error': 'Transcript not found. Please transcribe first.'}), 404
        
        transcript = data['transcript']
        
        # Generate summary
        print(f"Generating summary for {meeting_id}...")
        service = get_summarization_service()
        summary_result = service.summarize_meeting(transcript)
        
        # Update saved data
        data['summary'] = summary_result['summary']
        data['key_decisions'] = summary_result['key_decisions']
        data['action_items'] = summary_result['action_items']
        data['summary_timestamp'] = datetime.now().isoformat()
        save_result(meeting_id, data)
        
        return jsonify({
            'meeting_id': meeting_id,
            'summary': summary_result['summary'],
            'key_decisions': summary_result['key_decisions'],
            'action_items': summary_result['action_items'],
            'message': 'Summary generated successfully'
        }), 200
        
    except Exception as e:
        print(f"Error generating summary: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/process/<meeting_id>', methods=['POST'])
def process_meeting(meeting_id):
    """
    Process meeting: transcribe and summarize in one call
    
    Args:
        meeting_id: Unique meeting identifier
    
    Returns:
        JSON with complete results
    """
    try:
        # Find the audio file
        audio_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) 
                      if f.startswith(meeting_id)]
        
        if not audio_files:
            return jsonify({'error': 'Audio file not found'}), 404
        
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_files[0])
        
        # Step 1: Transcribe
        print(f"Starting transcription for {meeting_id}...")
        trans_service = get_transcription_service()
        trans_result = trans_service.transcribe_audio(audio_path)
        
        # Step 2: Summarize
        print(f"Generating summary for {meeting_id}...")
        summ_service = get_summarization_service()
        summary_result = summ_service.summarize_meeting(trans_result['transcript'])
        
        # Save complete result
        data = {
            'meeting_id': meeting_id,
            'timestamp': datetime.now().isoformat(),
            'transcript': trans_result['transcript'],
            'segments': trans_result['segments'],
            'language': trans_result['language'],
            'summary': summary_result['summary'],
            'key_decisions': summary_result['key_decisions'],
            'action_items': summary_result['action_items']
        }
        save_result(meeting_id, data)
        
        return jsonify({
            'meeting_id': meeting_id,
            'transcript': trans_result['transcript'],
            'language': trans_result['language'],
            'summary': summary_result['summary'],
            'key_decisions': summary_result['key_decisions'],
            'action_items': summary_result['action_items'],
            'message': 'Meeting processed successfully'
        }), 200
        
    except Exception as e:
        print(f"Error processing meeting: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/meetings', methods=['GET'])
def list_meetings():
    """Get list of all processed meetings"""
    try:
        meetings = []
        data_folder = app.config['DATA_FOLDER']
        
        if os.path.exists(data_folder):
            for filename in os.listdir(data_folder):
                if filename.endswith('.json'):
                    meeting_id = filename.replace('.json', '')
                    data = load_result(meeting_id)
                    if data:
                        meetings.append({
                            'meeting_id': meeting_id,
                            'timestamp': data.get('timestamp'),
                            'has_transcript': 'transcript' in data,
                            'has_summary': 'summary' in data
                        })
        
        return jsonify({'meetings': meetings}), 200
        
    except Exception as e:
        print(f"Error listing meetings: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/meetings/<meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    """Get full details of a specific meeting"""
    try:
        data = load_result(meeting_id)
        
        if not data:
            return jsonify({'error': 'Meeting not found'}), 404
        
        return jsonify(data), 200
        
    except Exception as e:
        print(f"Error retrieving meeting: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║          🎙️  MEETING SUMMARIZER - BACKEND API               ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    
    🚀 Backend server starting on http://localhost:{port}
    
    📋 API Endpoints:
       - GET  /api/health
       - POST /api/upload
       - POST /api/transcribe/<meeting_id>
       - POST /api/summarize/<meeting_id>
       - POST /api/process/<meeting_id>
       - GET  /api/meetings
       - GET  /api/meetings/<meeting_id>
    
    📖 Documentation: See API_DOCUMENTATION.md
    
    Press Ctrl+C to stop the server
    ══════════════════════════════════════════════════════════════
    """)
    
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
