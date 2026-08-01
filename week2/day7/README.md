# 📅 Day 7 - ReAct (Reason + Act)

## 📖 What I Learned

### 🔹 ReAct
- **ReAct** stands for **Reason + Act**.
- It enables an AI model to **think**, **use tools**, and then **answer** based on the tool's result.

### 🔹 How ReAct Works

```text
User Question
      ↓
Thought
      ↓
Action (Call a Tool)
      ↓
Observation (Tool Result)
      ↓
Repeat if Needed
      ↓
Final Answer
```

### 🔹 Tools
- Tools are external functions the AI can call to perform specific tasks.
- Examples:
  - `get_product_price()` → Gets a product's price.
  - `calculator()` → Performs calculations.

### 🔹 Observation
- The result returned by a tool.
- The AI uses this result to decide the next step.

### 🔹 Agent
- An AI agent follows the **Thought → Action → Observation** loop until it can produce the final answer.

---

## ✅ ReAct Flow

```text
Thought → Action → Observation → Final Answer
```

---

## ✅ Advantages
- Can use external tools instead of guessing.
- Produces more accurate and reliable answers.
- Handles multi-step reasoning problems.

---

## ✅ Key Takeaways
- ReAct = **Reason + Act**.
- The AI thinks before taking an action.
- Tools help the AI perform real-world tasks.
- Observations guide the next reasoning step.
- The process continues until the final answer is generated.