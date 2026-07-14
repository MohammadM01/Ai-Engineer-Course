import os
import json
import pdfplumber
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found.")

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"

pdf_path = r"D:\Resumes\Pratyush Sir Resume.pdf"

resume_text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            resume_text += text + "\n"

print("=" * 50)
print("Extracted Resume Text")
print("=" * 50)
print(resume_text)
print("=" * 50)
print(f"Total Characters: {len(resume_text)}")

if len(resume_text.strip()) == 0:
    raise ValueError("No text extracted from PDF. The PDF is likely scanned. Use OCR.")

hr_requirements = {
    "skills": [
        "Python",
        "Machine Learning",
        "SQL",
        "Git",
        "Docker"
    ],
    "projects": [
        "Chatbot",
        "Resume Parser"
    ],
    "experience": [
        "Internship"
    ]
}


class Resume(BaseModel):
    skills: list[str]
    experience: list[str]
    projects: list[str]


schema = Resume.model_json_schema()

system_prompt = f"""
You are an expert resume parser.

Extract the following information from the resume.

Return ONLY valid JSON according to this schema.

{schema}

Rules:
1. Extract every skill you find.
2. Extract all projects.
3. Extract all experience.
4. If something is missing, return an empty list.
5. Return ONLY JSON.
"""

user_prompt = f"""
Resume:

{resume_text}
"""

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_prompt
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format={"type": "json_object"}
)

ans = response.choices[0].message.content

print("\nRaw LLM Response:")
print(ans)

data = json.loads(ans)

resume = Resume(**data)


def calculate_match(hr_list, resume_list):
    hr_lower = [x.lower() for x in hr_list]
    resume_lower = [x.lower() for x in resume_list]

    matched = []

    for item in hr_lower:
        if item in resume_lower:
            matched.append(item)

    percentage = (len(matched) / len(hr_list)) * 100 if hr_list else 0

    return matched, percentage


matched_skills, skill_percent = calculate_match(
    hr_requirements["skills"],
    resume.skills
)

matched_projects, project_percent = calculate_match(
    hr_requirements["projects"],
    resume.projects
)

matched_experience, exp_percent = calculate_match(
    hr_requirements["experience"],
    resume.experience
)

overall = (skill_percent + project_percent + exp_percent) / 3

print("\n===== Resume Data =====")
print(resume)

print("\n===== Matching Report =====")
print(f"Matched Skills: {matched_skills}")
print(f"Skill Match: {skill_percent:.2f}%")

print(f"\nMatched Projects: {matched_projects}")
print(f"Project Match: {project_percent:.2f}%")

print(f"\nMatched Experience: {matched_experience}")
print(f"Experience Match: {exp_percent:.2f}%")

print(f"\nOverall Match Percentage: {overall:.2f}%")