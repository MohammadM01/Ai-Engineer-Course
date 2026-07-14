import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api error")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
role = "user"

prompt1 = "Explain Time travel in simple terms for a 10 year old."
prompt2 = "Write a rhyming alletration poem"
prompt3= "Hii"

prompts = [prompt1, prompt2,prompt3]

for prompt in prompts:
    message = {"role": role, "content": prompt}
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=50)
    usage = response.usage
    print(
        f"Prompt: {prompt} --> my_token : {usage.prompt_tokens}, completion_tokens : {usage.completion_tokens}, total_tokens : {usage.total_tokens}, Finish Reason : {response.choices[0].finish_reason}\n"
    )

# print(response.choices[0].message.content)
