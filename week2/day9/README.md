# 📅 Day 9 - Streaming Responses

## 📖 What I Learned

### 🔹 Streaming
- Streaming allows the AI to send the response **token by token** instead of waiting for the complete response.
- The output starts appearing immediately, making the application feel faster.

### 🔹 `stream=True`
- Setting `stream=True` enables streaming mode.
- The API returns a stream of response chunks instead of one complete response.

### 🔹 Chunks
- The streamed response is divided into small parts called **chunks**.
- Each chunk contains a small portion of the generated text.

### 🔹 Delta
- `chunk.choices[0].delta.content` contains the newly generated text in each chunk.
- If the content exists, it can be printed immediately.

### 🔹 `flush=True`
- `flush=True` forces Python to display the output instantly without waiting for the buffer.

---

## ✅ Streaming Flow

```text
User Prompt
      ↓
API Request (stream=True)
      ↓
Response received in Chunks
      ↓
Extract delta.content
      ↓
Print immediately
```

---

## ✅ Advantages
- Faster user experience.
- Real-time response generation.
- Useful for chatbots, AI assistants, and long responses.

---

## ✅ Key Takeaways
- `stream=True` enables real-time streaming.
- Responses are received as **chunks**.
- `delta.content` contains the latest generated text.
- `flush=True` prints the output instantly.
- Streaming improves responsiveness and user experience.