#audio.py
from moviepy.editor import VideoFileClip
import os
import sys

def process_audio(video_file_path):
    try:
        #extract audio and save as .mp3
        if os.path.exists(video_file_path):
            audio_result = "Reference-audio.mp3"
            video_clip = VideoFileClip(video_file_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(audio_result)
            print("Audio .mp3 extraction completed")
            video_clip.close()
            audio_clip.close()
            return audio_result
        else:
            print(f"Error: Video file {video_file_path} cannot be found.")

    except Exception as e:
        #print("Error:", str(e))
        print("audio extraction problem")
        sys.exit()


#Path = input("Input updated file path:")
#process_audio(Path)