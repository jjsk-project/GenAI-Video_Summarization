# transcript.py
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import re

#if there is any problem, one of the solution is to replace invalid characters
def clean_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)

def process_transcript(video_url):
    try:
        yt = YouTube(video_url)
        #download & save video transcripts
        transcripts = YouTubeTranscriptApi.get_transcript(yt.video_id)
        transcript_filename = f"Reference-transcript.txt"
        with open(transcript_filename, "w", encoding="utf-8") as file:
            for entry in transcripts: #if time is needed. 
        #        file.write(f"{entry['start']} - {entry['start'] + entry['duration']}\n")
                file.write(f"{entry['text']}")
        print("Transcript download completed")
        transcript_result = True
        return transcript_filename, transcript_result

    except Exception as e:
        transcript_result = False
        transcript_filename = "No transcript"
    return transcript_filename, transcript_result
