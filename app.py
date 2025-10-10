from google import genai
from dotenv import load_dotenv
from google.genai import types
import os
load_dotenv()



Gemini_api_key = os.getenv('Gemini_api_key')
LLM_MODEL = os.getenv('LLM_MODEL')


client = genai.Client(api_key=Gemini_api_key)



while True:
    user_query = input('Please Ask Question...')
    if user_query == 'exit':
        break
    response = client.models.generate_content(
        model=LLM_MODEL, contents=user_query
    )
    print(response.text)
git remote add origin https://github.com/KhushalDaiya/khushal.git