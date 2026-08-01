import os
import json
import uuid
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionMessageParam

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from prompt import system_prompt

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API Key not found")

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("profile.json", "r", encoding="utf-8") as file:
    profile = json.load(file)

profile_data = json.dumps(profile, indent=2)

conversations: dict[str, list[ChatCompletionMessageParam]] = {}


def get_messages(chat_id: str):

    if chat_id not in conversations:

        conversations[chat_id] = [
            {
                "role": "system",
                "content": system_prompt
                + "\n\nCandidate Information:\n\n"
                + profile_data,
            }
        ]

    return conversations[chat_id]


def generate(chat_id: str, question: str):

    messages = get_messages(chat_id)

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )

    answer = ""

    for chunk in stream:

        text = chunk.choices[0].delta.content

        if text:
            answer += text
            yield text

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


@app.get("/")
def home():

    return {
        "message": "AI Portfolio Backend is Running"
    }


@app.get("/new-chat")
def new_chat():

    chat_id = str(uuid.uuid4())

    return {
        "chat_id": chat_id
    }


@app.get("/chat")
def chat(chat_id: str, question: str):

    return StreamingResponse(
        generate(chat_id, question),
        media_type="text/plain"
    )