import config
from provider import ask_gemeni,ask_ollama,ask_opeAI

def model_name():
    if config.LLM_PROVIDER=="openai":
        return config.OPENAI_MODEL
    elif config.LLM_PROVIDER=="gemini":
        return config.GEMENI_MODEL
    elif config.LLM_PROVIDER=="ollama":
        return config.OLLAMA_MODEL

def check_setup():
    """Return a helpfu message if something is missing in .env, othervise None."""
    if config.LLM_PROVIDER not in("openai","gemeni","ollama"):
        return(
            "LLM_PROVIDER is '" + str(config.PROVIDER) + "'.\n"
            "please set LLM_PROVIDER to openai,gemini or ollama in the .env file"
        )
    if config.LLM_PROVIDER=="openai" and not config.OPENAI_API_KEY:
        return "OPENAI_API_KEY is missing.\nplease add your openAI API key to the .env file."
    if not model_name():
        return(
        "The Model name for "+ config.LLM_PROVIDER +"is missing.\n"
        "Please set "+config.LLM_PROVIDER.upper()+" _MODEL in the .env file"
        
    )
def ask_llm(message):
    if config.LLM_PROVIDER=="openai":
        return ask_opeAI(message)
    if config.LLM_PROVIDER=="gemeni":
        return ask_gemeni
    else:
        return ask_ollama(message)

def main():
    problem=check_setup()
    if problem:
        print(f"Error {problem}")
        return
    print("="*40)
    print("           Simple GENAI CLI Chatbot")
    print("\n Provider:", config.LLM_PROVIDER)
    print("Model:",model_name())

    while True:
        message=input("\You:").strip()
        if message in ("exit", "stop"):
            print("Byeeeee")
            break
        if not message:
            continue
        try:
            print(f"ASssiten:{ask_llm(message)}")
        except Exception as e:
            print(f"sorry, the request failed:{e}")
if __name__=="__main__":
     main()