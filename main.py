#main.py
import sys
from video import process_video
from transcript import process_transcript
from audio import process_audio
from use_whisper import whisper_to_text
from my_openai import my_openai
import openai

def main():
    video_url = input("Enter Youtube video URL: ") 
    #video_url = "https://youtu.be/y9YWvcZrxGQ?si=XjC8NDJ7Wj15WKzG" #we can hard code the video
    #video_url = "https://youtu.be/XsRpvWHIVw0?si=i39hCLW6-3sAM6ea" #no-sub example. Steve Jobs speech. Japanese
    transcript_filename, transcript_result = process_transcript(video_url)
    if transcript_result == True:
        #sys.exit() #Option:If transcript is available, stop. 
        print("Transcript is available and downloaded. Starting OpenAI-API-summarization.")
        pass 
    else: 
        print("No transcript.Starting video, audio, OpenAI-whisper-transcript processes")
        video_result = process_video(video_url)
        audio_result = process_audio(video_result)  
        text_result = whisper_to_text(audio_result)
        pass

    #Please create API and assistnat ID on OpenAI Playground or Use my_openai.py 
    api_key = "Please put your OpenAI API Key here"
    assistant_id = "Once Assistant ID is created, please put it here"
    client = openai.OpenAI(api_key=api_key)
    my_openai(api_key,client,assistant_id)
if __name__ == "__main__":
    main()
