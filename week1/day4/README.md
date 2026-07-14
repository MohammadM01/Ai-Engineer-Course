# 📅 Day 4 - Structured Output, JSON & Pydantic

## 📖 What I Learned

### 🔹 Structured Output
- Structured output ensures the AI returns data in a predefined format.
- It makes the response easy to parse and use in applications.

### 🔹 JSON Output
- JSON (JavaScript Object Notation) is a standard format for storing and exchanging data.
- AI can be instructed to return responses as valid JSON objects.

### 🔹 Pydantic
- Pydantic is a Python library used for data validation.
- It defines the expected structure of data using Python classes.
- It automatically validates the data types of each field.

### 🔹 BaseModel
- `BaseModel` is the parent class used to create data models in Pydantic.
- Each attribute represents a field in the structured output.

### 🔹 JSON Schema
- `model_json_schema()` generates a JSON schema from a Pydantic model.
- The schema tells the AI exactly what fields and data types are expected.

### 🔹 System Prompt
- The system prompt instructs the AI to return data according to the provided schema.
- This improves the consistency and accuracy of the output.

### 🔹 Response Format
- Setting:
  ```python
  response_format = {"type": "json_object"}
  ```
  forces the model to return a valid JSON object instead of plain text.

### 🔹 Parsing JSON
- `json.loads()` converts the JSON string returned by the AI into a Python dictionary.

### 🔹 Data Validation
- Passing the dictionary into a Pydantic model validates that all required fields exist and have the correct data types.

---

## ✅ Key Takeaways
- Learned how to generate structured AI responses.
- Understood the purpose of JSON and JSON Schema.
- Learned how Pydantic validates structured data.
- Used `BaseModel` to define the expected output format.
- Learned how `response_format` forces JSON responses.
- Converted JSON into Python objects using `json.loads()`.
- Validated AI-generated data using Pydantic models.