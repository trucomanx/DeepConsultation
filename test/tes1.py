import sys
sys.path.append("../src")


from deep_consultation.core import consult_with_deepchat

USER_MSG="Quanto é 2+2."

SYSTEM_MSG="You are an expert assistant with a spartan and stoic mentality"
    
API_KEY=input("API KEY: ")

BASE_URL="https://api.deepinfra.com/v1/openai"
MODEL="meta-llama/Meta-Llama-3.1-70B-Instruct"

#BASE_URL = ""
#MODEL = "gpt-5-mini"

OUT=consult_with_deepchat(BASE_URL,API_KEY,MODEL,USER_MSG,SYSTEM_MSG)
print(OUT)
