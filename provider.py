import requests #for Ollama response 
import config
from openai import OpenAI

def ask_opeAI(message):
    """send message to OpenAi and return the answer as text """
    #1-Client Baya
    client=OpenAI(api_key=config.OPENAI_API_KEY)#maine ye value config me nhi dali becase hamare mpass  API keys nahi hai ye bas samajh 
    #ne ke liye hai multi providers ko. hamara Provider hai Ollama
    
    #client ke through salwal jawab karne ke liye use karte hai
    #2- client ko call karke response nikal

    #this not type by instructor this code are given by  OpenAI they tells how take a response from me
    response=client.responses.create(
        model=config.OPENAI_MODEL,
        instructions=config.SYSTEM_PROMPT,
        input=message,
    )#Open AI rulse for create response
    #3-response se output nikala
    return response.output_text #give clean output only valuable info in form of text

    pass
def ask_gemeni(message):
    """Send a message and return the answer as text."""
    client = gemeni.client(api_key=config.GEMINI_API_KEY)
    #Google rule to create response
    response = client.responses.create(
        model=config.GEMINI_MODEL,
        instructions=config.SYSTEM_PROMPT,
        input=message,
    )
    return response.text
    
def ask_ollama(message):
    """THis is our main PROVIDER, sent mesage to Olama that returns answer as text running locally in ollama"""
    try:
        response = requests.post(
            config.OLLAMA_BASE_URL + "/api/chat",
            json={
                "model": config.OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": config.SYSTEM_PROMPT},#this is for role
                    {"role": "user", "content": message},#this is for 
                ],
                "stream": False,
            },
            timeout=120,
        )
    except requests.exceptions.ConnectionError as error:
        raise RuntimeError("Could not reach Ollama. Is it running locally?") from error

    response.raise_for_status()#
    return response.json()["message"]["content"]
