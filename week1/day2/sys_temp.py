import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api error")
client = Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
prompt="Suggest a name for my Food Brand."
message={
    "role": role,
    "content": prompt
}

message_system={
    "role": "system",
    "content": "You are a brand manager who suggests names for my food company. Name should be in one word and suggest only 1 name with meaning in short"
}

messages=[message_system, message]
response = client.chat.completions.create(model=model, messages=messages, temperature=2)

print(response.choices[0].message.content)