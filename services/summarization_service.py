"""
Summarization service using Google Gemini AI for generating meeting summaries
"""
import google.generativeai as genai
from typing import Dict, List
import os

class SummarizationService:
    def __init__(self, api_key: str = None):
        """
        Initialize the summarization service with Google Gemini
        
        Args:
            api_key: Google API key for Gemini
        """
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("Google API key is required. Set GOOGLE_API_KEY in .env file")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def summarize_meeting(self, transcript: str) -> Dict:
        """
        Generate a comprehensive meeting summary with key decisions and action items
        
        Args:
            transcript: The meeting transcript text
        
        Returns:
            Dictionary containing summary, key decisions, and action items
        """
        prompt = f"""
You are an expert meeting analyst. Analyze the following meeting transcript and provide:

1. A concise summary (2-3 paragraphs) of the meeting
2. Key decisions made during the meeting
3. Action items with clear ownership if mentioned

Meeting Transcript:
{transcript}

Please format your response as follows:

SUMMARY:
[Provide a comprehensive summary here]

KEY DECISIONS:
- [Decision 1]
- [Decision 2]
...

ACTION ITEMS:
- [Action item 1]
- [Action item 2]
...

If there are no key decisions or action items, explicitly state "None identified."
"""
        
        try:
            response = self.model.generate_content(prompt)
            result_text = response.text
            
            # Parse the response
            parsed_result = self._parse_summary_response(result_text)
            return parsed_result
            
        except Exception as e:
            print(f"Error generating summary: {e}")
            raise
    
    def _parse_summary_response(self, response_text: str) -> Dict:
        """
        Parse the LLM response into structured data
        
        Args:
            response_text: Raw text response from LLM
        
        Returns:
            Structured dictionary with summary, decisions, and action items
        """
        lines = response_text.strip().split('\n')
        
        summary_lines = []
        key_decisions = []
        action_items = []
        
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if 'SUMMARY:' in line.upper():
                current_section = 'summary'
                continue
            elif 'KEY DECISION' in line.upper():
                current_section = 'decisions'
                continue
            elif 'ACTION ITEM' in line.upper():
                current_section = 'actions'
                continue
            
            if not line or line.startswith('#'):
                continue
            
            if current_section == 'summary':
                summary_lines.append(line)
            elif current_section == 'decisions':
                if line.startswith('-') or line.startswith('•') or line.startswith('*'):
                    key_decisions.append(line.lstrip('-•* '))
                elif line and not any(x in line.upper() for x in ['ACTION', 'DECISION']):
                    key_decisions.append(line)
            elif current_section == 'actions':
                if line.startswith('-') or line.startswith('•') or line.startswith('*'):
                    action_items.append(line.lstrip('-•* '))
                elif line and not any(x in line.upper() for x in ['ACTION', 'DECISION']):
                    action_items.append(line)
        
        return {
            'summary': ' '.join(summary_lines).strip(),
            'key_decisions': [d for d in key_decisions if d],
            'action_items': [a for a in action_items if a],
            'raw_response': response_text
        }
    
    def generate_custom_summary(self, transcript: str, custom_prompt: str) -> str:
        """
        Generate a summary with a custom prompt
        
        Args:
            transcript: The meeting transcript
            custom_prompt: Custom instructions for summarization
        
        Returns:
            Summary text
        """
        full_prompt = f"{custom_prompt}\n\nTranscript:\n{transcript}"
        
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            print(f"Error generating custom summary: {e}")
            raise


def summarize_meeting(transcript: str, api_key: str = None) -> Dict:
    """
    Convenience function to summarize a meeting transcript
    
    Args:
        transcript: Meeting transcript text
        api_key: Optional Google API key
    
    Returns:
        Dictionary with summary, key decisions, and action items
    """
    service = SummarizationService(api_key=api_key)
    return service.summarize_meeting(transcript)
