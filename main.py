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
        print("Transcript is available and downloaded.")
        print("Still download the video and use OpenAI_whisper to generate transcription? Please input Y or Yes")
        still_download = input()
        #still_download = "Y"
        pass
    elif not transcript_result:
        still_download = "Y"
        print("Transcript is not available.")
        pass

    if still_download.lower() == "y" or still_download.lower() == "yes":
        print("Starting video, audio, OpenAI-whisper-transcript processes")
        video_result = process_video(video_url)
        audio_result = process_audio(video_result)  
        text_result = whisper_to_text(audio_result)
    else:
        print("No video download and processing.")

    #Please create API in OpenAI Playground
    api_key_input = input("Open AI API Key Here:")
    api_key = api_key_input
    assistant_id = "asst_dtae9QFKpbOFLkJFixCPfAjQ"
    print("Starting OpenAI-API-summarization.")
    client = openai.OpenAI(api_key=api_key)
    my_openai(api_key,client,assistant_id)
if __name__ == "__main__":
    main()
