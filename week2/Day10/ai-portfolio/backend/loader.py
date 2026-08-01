from pypdf import PdfReader
import json


def load_resume(path):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)