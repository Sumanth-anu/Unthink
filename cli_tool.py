"""
Simple command-line interface for Meeting Summarizer
Useful for quick testing without the web interface
"""
import os
import sys
from services import TranscriptionService, SummarizationService
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def print_banner():
    """Print application banner"""
    print("=" * 60)
    print("🎙️  Meeting Summarizer - CLI Version")
    print("=" * 60)
    print()

def process_audio_file(audio_path):
    """
    Process an audio file: transcribe and summarize
    
    Args:
        audio_path: Path to the audio file
    """
    if not os.path.exists(audio_path):
        print(f"Error: File not found: {audio_path}")
        return
    
    print(f"Processing: {audio_path}")
    print()
    
    # Step 1: Transcription
    print("Step 1: Transcribing audio...")
    print("(This may take a few minutes depending on file length)")
    print()
    
    try:
        transcription_service = TranscriptionService(model_size="base")
        result = transcription_service.transcribe_audio(audio_path)
        
        transcript = result['transcript']
        language = result['language']
        
        print(f"✓ Transcription complete!")
        print(f"  Language detected: {language}")
        print(f"  Transcript length: {len(transcript)} characters")
        print()
        
    except Exception as e:
        print(f"✗ Transcription failed: {e}")
        return
    
    # Step 2: Summarization
    print("Step 2: Generating summary with AI...")
    print()
    
    try:
        summarization_service = SummarizationService()
        summary_result = summarization_service.summarize_meeting(transcript)
        
        print("✓ Summary generated!")
        print()
        
    except Exception as e:
        print(f"✗ Summarization failed: {e}")
        print(f"   Note: Make sure GOOGLE_API_KEY is set in .env file")
        return
    
    # Display results
    print("=" * 60)
    print("RESULTS")
    print("=" * 60)
    print()
    
    print("📝 TRANSCRIPT")
    print("-" * 60)
    # Show first 500 characters
    print(transcript[:500] + ("..." if len(transcript) > 500 else ""))
    print()
    
    print("📋 SUMMARY")
    print("-" * 60)
    print(summary_result['summary'])
    print()
    
    print("🎯 KEY DECISIONS")
    print("-" * 60)
    if summary_result['key_decisions']:
        for i, decision in enumerate(summary_result['key_decisions'], 1):
            print(f"{i}. {decision}")
    else:
        print("No key decisions identified.")
    print()
    
    print("✅ ACTION ITEMS")
    print("-" * 60)
    if summary_result['action_items']:
        for i, action in enumerate(summary_result['action_items'], 1):
            print(f"{i}. {action}")
    else:
        print("No action items identified.")
    print()
    
    # Save results
    output_file = audio_path.rsplit('.', 1)[0] + '_summary.txt'
    save_results(output_file, transcript, summary_result)
    print(f"💾 Results saved to: {output_file}")
    print()

def save_results(output_file, transcript, summary_result):
    """Save results to a text file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("MEETING SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("TRANSCRIPT\n")
        f.write("-" * 60 + "\n")
        f.write(transcript + "\n\n")
        
        f.write("SUMMARY\n")
        f.write("-" * 60 + "\n")
        f.write(summary_result['summary'] + "\n\n")
        
        f.write("KEY DECISIONS\n")
        f.write("-" * 60 + "\n")
        if summary_result['key_decisions']:
            for i, decision in enumerate(summary_result['key_decisions'], 1):
                f.write(f"{i}. {decision}\n")
        else:
            f.write("None identified.\n")
        f.write("\n")
        
        f.write("ACTION ITEMS\n")
        f.write("-" * 60 + "\n")
        if summary_result['action_items']:
            for i, action in enumerate(summary_result['action_items'], 1):
                f.write(f"{i}. {action}\n")
        else:
            f.write("None identified.\n")

def main():
    """Main CLI function"""
    print_banner()
    
    if len(sys.argv) < 2:
        print("Usage: python cli_tool.py <audio_file>")
        print()
        print("Example:")
        print("  python cli_tool.py meeting.mp3")
        print()
        print("Supported formats: WAV, MP3, M4A, FLAC, OGG, WEBM")
        print()
        return
    
    audio_file = sys.argv[1]
    process_audio_file(audio_file)
    
    print("=" * 60)
    print("Processing complete! 🎉")
    print("=" * 60)

if __name__ == "__main__":
    main()
