# 📅 Day 13 - Basic RAG Pipeline

## 📖 What I Learned

### 🔹 Documents

* Created a small set of documents containing useful information.
* These documents act as our knowledge base.

### 🔹 Document Embeddings

* Converted all documents into **embeddings** using `SentenceTransformer`.
* Embeddings represent the meaning of the text as vectors.

### 🔹 Similarity Search

* Converted the user's question into an embedding.
* Compared the question with all document embeddings using **cosine similarity**.
* Selected the most similar document.

### 🔹 Context

* The retrieved document is passed to the LLM as **context**.
* The LLM uses this context to answer the question.

### 🔹 Groq LLM

* Used the Groq API to generate the final answer.
* The model is instructed to answer only from the retrieved context.

---

## ✅ RAG Flow

```text
    Documents
       ↓
Create Embeddings
       ↓
  User Question
       ↓
Question Embedding
       ↓
Cosine Similarity
       ↓
Best Matching Document
       ↓
Context + Question
       ↓
      LLM
       ↓
  Final Answer
```

---

## ✅ Key Takeaways

* Documents can be converted into embeddings.
* Embeddings can be compared using cosine similarity.
* The most relevant document can be retrieved.
* Retrieved information is given to the LLM as context.
* This is the basic idea behind a **RAG pipeline**.
