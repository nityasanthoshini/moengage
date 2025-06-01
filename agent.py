import os
from openai import OpenAI
from dotenv import load_dotenv  # <-- missing import

load_dotenv()  # <-- this line loads .env variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(prompt, model="gpt-4o"):
    print("Mock GPT called. Skipping actual OpenAI call due to quota limit.")
    return "⚠️ Mocked GPT response: Your quota is exhausted. This is a placeholder."

