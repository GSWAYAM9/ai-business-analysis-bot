from groq import Groq
from config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_text(prompt: str, model: str = "llama-3.1-8b-instant") -> str:
    try:
        print("🧠 Sending prompt to Groq AI...")

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior business analyst. Respond with clear, structured, actionable insights."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=800,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print("❌ GROQ AI FAILURE:", repr(e))
        return ""
