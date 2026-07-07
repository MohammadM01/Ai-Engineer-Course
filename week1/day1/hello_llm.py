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
prompt="Write a 4 line poem about the beauty of nature in poetic tone with rhyming verse."
message={
    "role": role,
    "content": prompt
}

messages=[message]
response = client.chat.completions.create(model=model, messages=messages)

print(response.choices[0].message.content)