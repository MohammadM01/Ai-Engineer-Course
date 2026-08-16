import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
print("I am connected to Qdrant Cloud!")

COLLECTION_NAME = "knowledge_base"
EMBEDDING_SIZE = 384

if client.collection_exists(COLLECTION_NAME):
    print(f"Deleting existing Collection:{COLLECTION_NAME}")
    client.delete_collection(COLLECTION_NAME)

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=EMBEDDING_SIZE, distance=Distance.COSINE),
)
print(f"Collection Created: {COLLECTION_NAME}")
print(f"Vector Size: {EMBEDDING_SIZE}")
print("Distance: Cosine")

with open("knowledge_base.txt", "r") as f:
    documents = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(documents)} documents")

print("Loading Embedding Model...")

model = SentenceTransformer("all-MiniLM-L6-v2")
print("Embedding Model ready!")
embeddings = model.encode(documents)
print(f"Generated {len(embeddings)} embeddings")
print(f"Embedding Size: {len(embeddings[0])}")

points = []
for i, embedding in enumerate(embeddings):
    point = PointStruct(
        id=i + 1, vector=embedding.tolist(), payload={"text": documents[i]}
    )
    points.append(point)

client.upsert(collection_name=COLLECTION_NAME, points=points)
print(f"Uploaded{len(points)} documents to Qdrant!")


def search(query, top_k=1):
    query_vector = model.encode(query).tolist()
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True,
    ).points
    return results


query = "How much vacation do I get?"
results = search(query, top_k=3)
print("\nSearch Results:")

for result in results:
    print(f"Scores: {result.score:.3f}")
    if result.payload is not None:
        print(result.payload["text"])
    print()

groq_client = Groq(api_key=GROQ_API_KEY)


def ask_llm(ques, context):
    prompt = f"""
    Answer the question only using the info provided below.
    Context: {context}
    Question: {ques}
    If the answer is not present in the context, say: "I don't know based on the provided Information."
    """
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


ques = "How much vacation days do I get?"
results = search(ques, top_k=3)

context = "\n".join(
    result.payload["text"]
    for result in results
    if result.payload is not None
)

ans = ask_llm(ques, context)
print("Final Answer:")
print(ans)
