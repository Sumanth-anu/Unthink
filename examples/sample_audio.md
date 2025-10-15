# Sample Audio for Testing

Since this repository doesn't include actual audio files, you'll need to provide your own test audio.

## Where to Get Test Audio

### 1. Record Your Own
- Use your phone or computer to record a short meeting or conversation
- Export in MP3, WAV, or M4A format
- Keep it under 5 minutes for faster testing

### 2. Use Free Sample Audio
- **Common Voice**: https://commonvoice.mozilla.org/
- **LibriVox**: https://librivox.org/ (public domain audiobooks)
- **Free Music Archive**: https://freemusicarchive.org/

### 3. Create Test Audio with Text-to-Speech
Use online TTS services to generate sample meeting audio:
- Google Text-to-Speech
- Amazon Polly
- Natural Readers

## Sample Meeting Script

If you want to create test audio, here's a sample meeting script you can record or convert to speech:

```
Speaker 1: Good morning everyone, thank you for joining today's product planning meeting. Today we need to discuss our Q1 roadmap and prioritize the features for our next release.

Speaker 2: Thanks for organizing this. I think our main focus should be on improving the user authentication system. We've had several customer requests about adding two-factor authentication.

Speaker 1: That's a great point. Let's make that a priority. What about the mobile app redesign that was proposed last month?

Speaker 3: I think we should postpone the mobile redesign to Q2. Our development team is already stretched thin, and authentication security is more critical right now.

Speaker 1: Agreed. So our key decision here is to implement two-factor authentication as the top priority for Q1, and move the mobile redesign to Q2.

Speaker 2: I'll take the action item to create a technical specification for the 2FA implementation by next Friday.

Speaker 3: And I can research authentication vendors and prepare a comparison report by the end of next week.

Speaker 1: Perfect. Let's also schedule a security audit for early February to ensure everything is properly implemented. I'll coordinate that.

Speaker 2: Sounds good. What about the budget for this project?

Speaker 1: We've allocated fifty thousand dollars for security improvements this quarter. That should be sufficient for the 2FA implementation and the security audit.

Speaker 3: Excellent. I think we have a clear plan then.

Speaker 1: Great work everyone. To summarize: We're prioritizing two-factor authentication for Q1, postponing the mobile redesign, and conducting a security audit in February. Action items are assigned. Let's reconvene next week to review progress. Thanks everyone!
```

## Expected Output for Sample Script

When you process this audio, you should get:

**Summary:**
The meeting focused on Q1 product planning with emphasis on security improvements. The team decided to prioritize two-factor authentication implementation over the mobile app redesign, which was postponed to Q2. Budget allocation of $50,000 for security improvements was confirmed, and a security audit was scheduled for February.

**Key Decisions:**
- Implement two-factor authentication as top priority for Q1
- Postpone mobile app redesign to Q2
- Allocate $50,000 budget for security improvements
- Schedule security audit for early February

**Action Items:**
- Create technical specification for 2FA implementation (Assigned to Speaker 2, Due: Next Friday)
- Research authentication vendors and prepare comparison report (Assigned to Speaker 3, Due: End of next week)
- Coordinate security audit (Assigned to Speaker 1, Due: Early February)

## Testing Tips

1. **Audio Quality**: Use clear audio with minimal background noise for best results
2. **Length**: Start with 1-3 minute files for faster testing
3. **Format**: MP3 and WAV work best
4. **Content**: Meetings with clear decisions and action items work best for demonstrating the AI capabilities
5. **Multiple Speakers**: While the system works with multiple speakers, transcription will be more accurate with single speaker or clear audio

## Using the Test Script

```bash
# Make sure the server is running
python app.py

# In another terminal, run the test script
python examples/test_api.py path/to/your/audio.mp3
```
