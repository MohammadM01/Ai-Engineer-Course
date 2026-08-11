# 📅 Day 12 - Embeddings & Cosine Similarity

## 📖 What I Learned

### 🔹 Embeddings

- Embeddings convert text into **numbers (vectors)**.
- Similar meanings produce similar vectors.
- I used `SentenceTransformer` with the `all-MiniLM-L6-v2` model.

### 🔹 SentenceTransformer

- `SentenceTransformer` converts sentences into embeddings.
- `model.encode()` is used to create the embedding.

### 🔹 Cosine Similarity

- Cosine similarity measures how similar two vectors are.
- A value closer to **1** means the texts are more similar.
- A value closer to **0** means the texts are less similar.

### 🔹 Example

```text
"There are 24 paid leaves"

"There are 24 vacation days"
```
### 🔹 Flow
```
Text
  ↓
SentenceTransformer
  ↓
Embedding / Vector
  ↓
Cosine Similarity
  ↓
Similarity Score
```

### ✅ Key Takeaways
- Embeddings represent text as vectors.
- model.encode() creates embeddings.
- Cosine similarity compares embeddings.
- Similar sentences have higher similarity scores.
- Embeddings are an important part of RAG and semantic search.