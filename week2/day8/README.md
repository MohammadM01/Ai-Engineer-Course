# 📅 Day 8 - Prompt Chaining

## 📖 What I Learned

### 🔹 Prompt Chaining
- Prompt Chaining is the process of connecting multiple AI prompts where the output of one prompt becomes the input for the next prompt.
- It helps solve complex tasks by breaking them into smaller steps.

### 🔹 Why Use Chaining?
- Improves accuracy.
- Makes prompts simpler and easier to manage.
- Creates structured AI workflows.
- Reduces prompt complexity.

### 🔹 Chaining Workflow

```text
Resume
   ↓
Extract Candidate Skills
   ↓
Job Description
   ↓
Extract Required Skills
   ↓
Compare Skills
   ↓
Generate Match Score & Verdict
```

### 🔹 Step 1 - Resume Skill Extraction
- Extract only the candidate's skills from the resume.
- Return the skills as a comma-separated list.

### 🔹 Step 2 - Job Description Skill Extraction
- Extract only the required skills from the job description.
- Return the skills as a comma-separated list.

### 🔹 Step 3 - Skill Matching
- Compare the candidate's skills with the required skills.
- Generate:
  - Match score (1–100)
  - Short hiring verdict

---

## ✅ Advantages
- Breaks large tasks into smaller, manageable steps.
- Produces more reliable outputs.
- Easy to debug and improve each step independently.
- Reusable for multi-step AI applications.

---

## ✅ Key Takeaways
- Prompt Chaining connects multiple AI prompts.
- Each step's output is used as the next step's input.
- Smaller prompts generally produce better results.
- Ideal for workflows like resume screening, document analysis, summarization, and data extraction.