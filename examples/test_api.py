"""
Example script to test the Meeting Summarizer API
"""
import requests
import json
import time
import os

BASE_URL = "http://localhost:5000"

def test_health():
    """Test the health endpoint"""
    print("\n=== Testing Health Endpoint ===")
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def upload_audio(file_path):
    """Upload an audio file"""
    print("\n=== Uploading Audio File ===")
    
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return None
    
    with open(file_path, 'rb') as f:
        files = {'audio': f}
        response = requests.post(f"{BASE_URL}/api/upload", files=files)
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)}")
        return data.get('meeting_id')
    else:
        print(f"Error: {response.text}")
        return None

def process_meeting(meeting_id):
    """Process a meeting (transcribe + summarize)"""
    print(f"\n=== Processing Meeting {meeting_id} ===")
    print("This may take a few minutes depending on audio length...")
    
    response = requests.post(f"{BASE_URL}/api/process/{meeting_id}")
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("\n--- Results ---")
        print(f"Meeting ID: {data.get('meeting_id')}")
        print(f"Language: {data.get('language')}")
        print(f"\nTranscript Preview: {data.get('transcript', '')[:200]}...")
        print(f"\nSummary: {data.get('summary', '')[:300]}...")
        print(f"\nKey Decisions: {len(data.get('key_decisions', []))} found")
        for i, decision in enumerate(data.get('key_decisions', [])[:3], 1):
            print(f"  {i}. {decision}")
        print(f"\nAction Items: {len(data.get('action_items', []))} found")
        for i, action in enumerate(data.get('action_items', [])[:3], 1):
            print(f"  {i}. {action}")
        return data
    else:
        print(f"Error: {response.text}")
        return None

def get_meeting_details(meeting_id):
    """Get details of a specific meeting"""
    print(f"\n=== Getting Meeting Details for {meeting_id} ===")
    
    response = requests.get(f"{BASE_URL}/api/meetings/{meeting_id}")
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)[:500]}...")
        return data
    else:
        print(f"Error: {response.text}")
        return None

def list_all_meetings():
    """List all processed meetings"""
    print("\n=== Listing All Meetings ===")
    
    response = requests.get(f"{BASE_URL}/api/meetings")
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        meetings = data.get('meetings', [])
        print(f"Found {len(meetings)} meetings:")
        for meeting in meetings:
            print(f"  - {meeting['meeting_id']} (Transcript: {meeting['has_transcript']}, Summary: {meeting['has_summary']})")
        return meetings
    else:
        print(f"Error: {response.text}")
        return []

def run_full_test(audio_file_path):
    """Run a complete test workflow"""
    print("=" * 60)
    print("Meeting Summarizer API Test")
    print("=" * 60)
    
    # Test health
    if not test_health():
        print("Health check failed! Make sure the server is running.")
        return
    
    # Upload audio
    meeting_id = upload_audio(audio_file_path)
    if not meeting_id:
        print("Upload failed!")
        return
    
    # Process meeting
    result = process_meeting(meeting_id)
    if not result:
        print("Processing failed!")
        return
    
    # Get meeting details
    get_meeting_details(meeting_id)
    
    # List all meetings
    list_all_meetings()
    
    print("\n" + "=" * 60)
    print("Test completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        audio_file = sys.argv[1]
        run_full_test(audio_file)
    else:
        print("Usage: python test_api.py <path_to_audio_file>")
        print("\nExample:")
        print("  python test_api.py meeting.mp3")
        print("\nOr test individual endpoints:")
        print("  - test_health()")
        print("  - upload_audio('path/to/file.mp3')")
        print("  - process_meeting('meeting_id')")
        print("  - list_all_meetings()")
