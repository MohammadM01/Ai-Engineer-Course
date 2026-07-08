# 📅 Day 1 - Groq API Basics

## 📖 What I Learned

### 🔹 Imports
- `os` → Access environment variables.
- `dotenv` → Load variables from the `.env` file.
- `Groq` → Connect Python with the Groq API.

### 🔹 API Key
- Store the API key securely in a `.env` file.
- Retrieve it using `os.getenv()`.
- Check if the key exists before making requests.

### 🔹 Client
- Create a Groq client using the API key.
- The client is responsible for communicating with the AI model.

### 🔹 Model
- The model determines which LLM will generate the response.
- Example: `llama-3.3-70b-versatile`

### 🔹 Prompt
- A prompt is the instruction or question given to the AI.
- A clear prompt usually produces better responses.

### 🔹 Roles
There are three main roles:
- **System** → Defines the AI's behavior or personality.
- **User** → Contains the user's request.
- **Assistant** → Represents the AI's previous response.

### 🔹 Messages
- The API accepts a **list of messages**, not a single message.
- Each message contains:
  - `role`
  - `content`
- Multiple messages help maintain conversation context.

### 🔹 Response
- The AI's generated answer is returned inside the response object.
- Extract the content from the response to display the output.

---


## ✅ Key Takeaways
- Learned the basic structure of using the Groq API.
- Understood the purpose of imports, API key, client, model, prompt, roles, messages, and response.
