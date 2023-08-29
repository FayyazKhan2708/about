from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

VIDEO_URL = 'paste the youtube video link here'

# Create a YouTube object
yt = YouTube("url")

# Get the video ID from the URL
video_id = yt.video_id

# Get the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Create a .txt file to save the transcript
output_file = f"transcript.txt"

with open(output_file, 'w', encoding='utf-8') as f:
    for entry in transcript:
        text = entry['text']
        f.write(text + '\n')

print(f"Transcript saved to {output_file}")

# Use the generated .txt file and paste the generated file name in transcriptSummary.py
