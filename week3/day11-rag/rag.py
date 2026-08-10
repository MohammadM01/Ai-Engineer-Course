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


knowledge_base = {
    "about":"Mohammad Mulla is a software engineer and a tech enthusiast. He is graduated from Shivajirao S. Jondhale College of Engineering, Dombivli, India.",
    "age":"Mohammad Mulla is 21 Years old"
}

def retrive_info(ques):
    ques=ques.lower()
    if "about" in ques:
        return knowledge_base["about"]
    elif "age" in ques:
        return knowledge_base["age"]
    else:
        return "Information not found."


def ask_llm(ques):
    context= retrive_info(ques)
    system_prompt=f"""Answer in one line and answer only based on this context do not hallucinate. Context: {context}"""
    system_message={
        "role": "system",
        "content": system_prompt
    }
    message={
        "role": "user",
        "content": ques
    }
    messages=[system_message, message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans

ques="What is Mohammad's age?"
print(ask_llm(ques))