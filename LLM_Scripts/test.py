import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro')

response = model.generate_content("What is the capital of France")
print(response)

print('IP:')
print(response.usage_metadata.prompt_token_count)