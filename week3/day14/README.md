\# 📅 Day 14 - Qdrant Vector Database



\## 📖 What I Learned



\### 🔹 Qdrant



\* Qdrant is a \*\*vector database\*\*.

\* It stores embeddings and helps us search for similar information.



\### 🔹 Collection



\* Created a Qdrant collection called `knowledge\_base`.

\* The vector size is \*\*384\*\*.

\* Used \*\*Cosine similarity\*\* to compare vectors.



\### 🔹 Uploading Documents



\* Loaded documents from `knowledge\_base.txt`.

\* Converted each document into an embedding using `SentenceTransformer`.

\* Stored the embeddings and text in Qdrant.



\### 🔹 Similarity Search



\* Converted the user's question into an embedding.

\* Searched Qdrant for the most similar documents.

\* Used `top\_k` to get the best matching results.



\### 🔹 RAG with Qdrant



\* Retrieved relevant documents from Qdrant.

\* Combined them into a context.

\* Sent the context and question to the Groq LLM.

\* The LLM generated the final answer using the retrieved information.



\---



\## ✅ RAG Flow



```text

Documents

&#x20;   ↓

Embeddings

&#x20;   ↓

Qdrant Vector Database

&#x20;   ↓

User Question

&#x20;   ↓

Question Embedding

&#x20;   ↓

Similarity Search

&#x20;   ↓

Relevant Documents

&#x20;   ↓

Context

&#x20;   ↓

Groq LLM

&#x20;   ↓

Final Answer

```



\---



\## ✅ Key Takeaways



\* Qdrant stores and searches \*\*vector embeddings\*\*.

\* `SentenceTransformer` creates the embeddings.

\* Cosine similarity finds similar information.

\* `top\_k` controls how many results are retrieved.

\* Retrieved documents become the \*\*context\*\* for the LLM.

\* Qdrant makes the RAG pipeline more practical and scalable.



