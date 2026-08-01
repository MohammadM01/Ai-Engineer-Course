import os
import json
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionMessageParam
from prompt import system_prompt

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API Key not found")

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"

with open("profile.json", "r", encoding="utf-8") as file:
    profile = json.load(file)

profile_data = json.dumps(profile, indent=2)

messages: list[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": system_prompt + "\n\nCandidate Information:\n\n" + profile_data
    }
]

while True:

    question = input("You : ")

    if question.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content

    if answer is None:
        answer = ""

    print("\nAI :", answer)
    print()

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )