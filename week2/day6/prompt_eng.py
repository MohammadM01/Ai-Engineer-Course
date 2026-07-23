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

def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans =response.choices[0].message.content
    return ans


bad_prompts = """
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK:
You have to classify the issue in a category
#CONSTRAINT:
You have to classify the issue in one of the 3 categories mainly Billing , Technical , Return
#OUTPT Format:
Your answer should be in one word only. The one word should be one of the catergories given to you in constraints.
#Example:
For instance if a user complain says he want a refund then the category is return
#FALLBACK:
If the issue is unrelated to any of the categories mentioned in constraints then the answer should be OTHER
This is a user complain:
My laptop is not working
I am not happy with my mobile
"""

print(llm_ans(bad_prompts))
