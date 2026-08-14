import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
from groq import Groq
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api error")

client = Groq(api_key=my_api_key)
groq_model = "llama-3.3-70b-versatile"

documents = [
    "Employees receive 24 days of paid leave per year.",
    "Employees work from the office on Tuesday, Wednesday and Thursday. "
    "Monday and Friday are optional work-from-home days.",
    "Employees receive Rs 3000 per month for gym reimbursement.",
    "Employees can claim Rs 2000 per month for home internet.",
    "Employees have a 90 day notice period."
]

document_embeddings = model.encode(documents)

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
    
    
def retrive(q_embeddings):
    scores = []
    for i, document in enumerate(document_embeddings):
        score = cosine_similarity(q_embeddings, document)
        scores.append((score, documents[i]))
    scores.sort(reverse=True)
    return scores[0]    

def ask_llm(ques, context):
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
    response = client.chat.completions.create(model=groq_model, messages=messages)
    ans=response.choices[0].message.content
    return ans
    
query = "How much vacation do I get?"
q_embedding = model.encode(query)

scores, context = retrive(q_embedding)
ans = ask_llm(query, context)
print(ans)