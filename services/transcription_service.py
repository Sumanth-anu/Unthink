"""
Transcription service using OpenAI Whisper (local) for audio-to-text conversion
"""
import whisper
import os
from typing import Dict

class TranscriptionService:
    def __init__(self, model_size: str = "base"):
        """
        Initialize the transcription service with Whisper
        
        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
                       - tiny: fastest, least accurate
                       - base: good balance (recommended)
                       - small: better accuracy
                       - medium/large: best accuracy, slower
        """
        print(f"Loading Whisper {model_size} model...")
        self.model = whisper.load_model(model_size)
        print("Whisper model loaded successfully!")
    
    def transcribe_audio(self, audio_path: str, language: str = None) -> Dict:
        """
        Transcribe audio file to text
        
        Args:
            audio_path: Path to the audio file
            language: Optional language code (e.g., 'en', 'es')
        
        Returns:
            Dictionary containing transcript and segments
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        print(f"Transcribing audio file: {audio_path}")
        
        # Transcribe with Whisper
        result = self.model.transcribe(
            audio_path,
            language=language,
            task="transcribe",
            verbose=False
        )
        
        # Extract full transcript
        transcript = result['text'].strip()
        
        # Extract segments with timestamps
        segments = []
        for segment in result['segments']:
            segments.append({
                'start': segment['start'],
                'end': segment['end'],
                'text': segment['text'].strip()
            })
        
        return {
            'transcript': transcript,
            'segments': segments,
            'language': result.get('language', 'unknown')
        }
    
    def transcribe_with_timestamps(self, audio_path: str) -> str:
        """
        Transcribe audio with formatted timestamps
        
        Args:
            audio_path: Path to the audio file
        
        Returns:
            Formatted transcript with timestamps
        """
        result = self.transcribe_audio(audio_path)
        
        formatted_transcript = []
        for segment in result['segments']:
            timestamp = self._format_timestamp(segment['start'])
            formatted_transcript.append(f"[{timestamp}] {segment['text']}")
        
        return '\n'.join(formatted_transcript)
    
    @staticmethod
    def _format_timestamp(seconds: float) -> str:
        """Format seconds into MM:SS timestamp"""
        mins = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{mins:02d}:{secs:02d}"


# For backward compatibility and easy import
def transcribe_audio(audio_path: str, model_size: str = "base") -> Dict:
    """
    Convenience function to transcribe audio
    
    Args:
        audio_path: Path to audio file
        model_size: Whisper model size
    
    Returns:
        Transcription result dictionary
    """
    service = TranscriptionService(model_size=model_size)
    return service.transcribe_audio(audio_path)
