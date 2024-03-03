# video.py
from pytube import YouTube
from moviepy.editor import VideoFileClip
import re
import os
import sys

def clean_filename(filename): #This can fix some bugs.
    return re.sub(r'[\/:*?"<>|！｜]', '', filename)

def process_video(video_url,resolution=360):
    try:
        #Download youtube video, input url
        yt = YouTube(video_url)
        #highest resolution video stream
        #video_stream = yt.streams.get_highest_resolution()
        video_stream = yt.streams.get_by_resolution(resolution)
        print("Downloading video. Video title: ", yt.title)
        video_stream.download(filename="Reference-video.mp4")
        video_file_path = f"Reference-video.mp4"
        print("Video download completed")
        return video_file_path

    except Exception as e:
        print("Error:", str(e))
        print("video download error")
        sys.exit()
        
