import os
from dotenv import load_dotenv  #this module are used to load value  of env secreately / 
#installing by using pasting pip install python-dotenv openai this command into terminal


# Load variables from .env into the system environment
load_dotenv()

# Read the environment variables into Python constants
LLM_PROVIDER = os.getenv("LLM_PROVIDER","openai")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT","you are help full assitance")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL","qwen2.5:3b")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")