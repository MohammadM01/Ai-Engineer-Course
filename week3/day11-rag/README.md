# 📅 Day 11 - RAG Basics

## 📖 What I Learned

### 🔹 RAG
- RAG stands for **Retrieval-Augmented Generation**.
- It first finds useful information and then gives it to the LLM.
- This helps the AI give better and more relevant answers.

### 🔹 Knowledge Base
- A knowledge base stores information that the AI can use.
- Today I created a simple knowledge base using a Python dictionary.

### 🔹 Retrieval
- Retrieval means finding the right information from the knowledge base.
- The retrieved information is given to the LLM as context.

### 🔹 Context
- Context is the information given to the LLM before answering.
- The LLM uses this context to generate the answer.

### 🔹 Hallucination
- RAG can help reduce hallucinations.
- The AI is instructed to answer only from the given context.

---

## ✅ RAG Flow

```text
User Question
      ↓
Retrieve Information
      ↓
Knowledge Base
      ↓
Give Context to LLM
      ↓
Final Answer
```

### ✅ Key Takeaways
- RAG = Retrieve + Generate
- Retrieval finds useful information.
- Context is given to the LLM.
- RAG helps reduce hallucinations.
- RAG is useful for AI chatbots and assistants.