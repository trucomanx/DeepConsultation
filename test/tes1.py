import sys
sys.path.append("../src")


from deep_consultation.core import consult_with_deepchat

USER_MSG='''Pelo que se observa, 
a palavra ``batuque'' não se usava para se referir a uma dança em particular mas sim aos festejos dos negros em geral \cite[pp. 85]{sandroni2001feitico}.
'''

SYSTEM_MSG='''You are an expert system that detects spelling, grammar, punctuation, coherence or cohesion errors in latex texts in any language.
    If you find no errors, only return the text "<NOERROR>".
    If you find errors, without any further response comment, only return a corrected version of the text respecting line breaks and try to make the least amount of changes possible, respecting the spirit of the content.
    The review will be done on each text that you receive from the user.'''
    
API_KEY=input("API KEY DEEPINFRA: ")

BASE_URL="https://api.deepinfra.com/v1/openai"

MODEL="meta-llama/Meta-Llama-3.1-70B-Instruct"

OUT=consult_with_deepchat(BASE_URL,API_KEY,MODEL,USER_MSG,SYSTEM_MSG)
print(OUT)
