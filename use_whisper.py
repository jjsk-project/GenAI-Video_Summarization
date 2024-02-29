#use_whisper.py
import whisper
import torch
import os

def whisper_to_text(audio_result):
    #check if CUDA is available = True. Much faster to use CUDA
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA is available. Using GPU.")
    else: #CUDA =! True
        device = torch.device("cpu") 
        print("CUDA is not available.")
    #Use Whisper. There are diff model sizes. 
    model = whisper.load_model("small").to(device) 
    #transcribe using the loaded model
    result = model.transcribe(audio_result, fp16=False)
    transcribed_text = result["text"]
    print(transcribed_text)
    output_txt_file = "Reference-transcript.txt"
    if os.path.exists(output_txt_file):
        try:
            os.remove(output_txt_file)
            print(f"Deleted existing {output_txt_file} file.")
        except Exception as e:
            print(f"Error deleting {output_txt_file}: {e}")
    with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write("Summarize these follow paragraphs into dot points:" + transcribed_text)
    print("whisper to audio completed!")
    return transcribed_text

