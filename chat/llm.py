import google.generativeai as genai

from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")


def ask_llm(messages) -> str:
    prompt = "\n".join(f"{m['role']}: {m['content']}" for m in messages)

    response = model.generate_content(prompt)
    return response.text
