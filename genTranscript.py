from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Replace 'VIDEO_URL' with the URL of the YouTube video
VIDEO_URL = 'https://www.youtube.com/watch?v=J_z-W4UVHkw'

# Create a YouTube object
yt = YouTube(VIDEO_URL)

# Get the video ID from the URL
video_id = yt.video_id

# Get the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Create a .txt file to save the transcript
output_file = f"{video_id}_transcript.txt"

with open(output_file, 'w', encoding='utf-8') as f:
    for entry in transcript:
        text = entry['text']
        f.write(text + '\n')

print(f"Transcript saved to {output_file}")
