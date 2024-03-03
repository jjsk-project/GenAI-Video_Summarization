#my_openai.py
import openai 
import os
import time
import logging
import re
from datetime import datetime

#if txt file is too big, cutting it to smaller chunks.
def chunk_text(text):
    chunks = []
    max_length = 30000  #chunk size
    for i in range(0, len(text), max_length):
        chunks.append(text[i:i+max_length])
    return chunks 

def create_openai_assistant():
    #==Create Secretary==# 
    model = "gpt-3.5-turbo-16k"
    client = openai.OpenAI(api_key=api_key)
    secretary_assis = client.beta.assistants.create(
        name="Secretary-001",
        instructions = """
        You are a secretary with finance and macroeconomic background. 
        You know how to understand content and provide summarization on each topic. 
        The summarizations are presented in related group of dot points. 
        """,
        model=model
    )
    assistant_id = secretary_assis.id
    print(assistant_id)
        #Option: Creating new secretary everytime


#def my_openai(api_key,client,thread_id,assistant_id): #Option: use particular thread
def my_openai(api_key,client,assistant_id): 
    openai.api_key = os.environ["OPENAI_API_KEY"]=api_key
    model = "gpt-3.5-turbo-16k"
    #===Thread===#
    thread = client.beta.threads.create(
        messages=[
            {   "role":"user",
                "content":"Please summarize the paragraphs in sequence."
            }
        ]
    )
    thread_id=thread.id
    print(f"OpenAI thread_id:'{thread_id}' \n")
    
    #===Reading file===#
    filename = "Reference-transcript.txt"
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            #print(content)
        content_chunks = chunk_text(content)
        for chunks in content_chunks:
            message = f"summarize in dot pints according to sequence in the paragraph and group similar topic together : {chunks}"
            message = client.beta.threads.messages.create(
                thread_id = thread_id,
                role = "user",
                content = message
            )
            #==Run our assistant==#
            run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id,
            )
            run_completion(client=client, thread_id=thread_id, run_id=run.id)
    else:
        print(f"The file '{filename}' does not exist.")
    
def run_completion(client,thread_id,run_id,sleep_interval=5):
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id,run_id=run_id)
            if run.completed_at: 
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"==Run completed in {formatted_elapsed_time}==")
                logging.info(f"Run completed in {formatted_elapsed_time}")
                # get message here once run is completed
                messages=client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"==Assistant Response:== \n{response}")
                break
        except Exception as e:
            logging.error(f"Error:Retriving the message")
            break
        logging.info("Logging \n")
        time.sleep(sleep_interval)


if __name__ == "__main__":
    api_key = "OpenAI API Key Here"
    
    #assistant_id = "Please put your assistant ID here"
    #thread_id = "thread_yf0uppwWmNr2FIpc8Dhb2Mbl"
    #client = openai.OpenAI(api_key=api_key)
    #my_openai(api_key, client, thread_id, assistant_id)
    #my_openai(api_key,client,assistant_id)

    #create_openai_assistant()
