import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_message(text: str) -> str:
    """
    Analyze a message and return:
    - Summary
    - Action items
    - Deadlines
    - Priority
    """
    if not os.getenv("OPENAI_API_KEY"):
        return "OPENAI_API_KEY is missing. Add it to your .env file."

    prompt = f"""
    You are an assistant that extracts useful information from messages.

    Return clearly formatted sections:

    Summary:
    - bullet points

    Action Items:
    - bullet points

    Deadlines:
    - bullet points

    Priority:
    (Low, Medium, High)

    Message:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content or "No response generated."
