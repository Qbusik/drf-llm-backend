import google.generativeai as genai

from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")


def ask_llm(prompt: str) -> str:

    response = model.generate_content(prompt)

    return response.text
