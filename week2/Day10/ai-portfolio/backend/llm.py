import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-120b"


def ask_llm(messages):

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
    )

    return response