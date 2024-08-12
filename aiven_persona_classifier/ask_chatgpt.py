import requests
import json
import io
from dotenv import load_dotenv
import os

load_dotenv()


# Function to call the GPT API from Python
def ask_chatgpt(prompt):
    # api_key = ""  # Don't share this! 😅
    api_key = os.getenv("OPENAI_API_KEY")  # Don't share this! 😅
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        # "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        # Handle errors or unexpected response status codes
        print(f"Error: Received response code {response.status_code}")
        return None
