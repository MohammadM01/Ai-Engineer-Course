# 📅 Day 6 - Prompt Engineering

## 📖 What I Learned

### 🔹 Prompt Engineering
- Prompt Engineering is the process of writing clear and effective prompts to get better AI responses.

### 🔹 A Good Prompt Should Include

#### 1. Role
- Defines who the AI should act as.
- Example: *"You are a customer support assistant."*

#### 2. Task
- Clearly tells the AI what to do.
- Example: *"Classify the user's issue."*

#### 3. Constraints
- Specifies the rules the AI must follow.
- Example:
  - Only choose from: `Billing`, `Technical`, `Return`.
  - Answer in **one word only**.

#### 4. Output Format
- Defines how the response should look.
- Example:
  - Return only one category.
  - No explanation.

#### 5. Example (Few-shot Prompting)
- Gives sample input and output.
- Helps the model understand the expected response.

#### 6. Fallback
- Tells the AI what to do if the request doesn't match the task.
- Example:
  - Return `OTHER`.

---

## ✅ Prompt Template

```text
ROLE:
Who the AI should be.

TASK:
What the AI should do.

CONSTRAINTS:
Rules the AI must follow.

OUTPUT FORMAT:
Expected response format.

EXAMPLE:
Sample input and output.

FALLBACK:
What to do if the request doesn't fit.
```

---

## ✅ Key Takeaways
- Clear prompts produce better results.
- Always define **Role**, **Task**, and **Constraints**.
- Specify the **Output Format**.
- Add **Examples** to improve accuracy.
- Use a **Fallback** for unexpected inputs.