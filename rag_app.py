import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
     print("GEMINI_API_KEY is not set") 
else:
     print("GEMINI_API_KEY is set")
     
app = FastAPI()
