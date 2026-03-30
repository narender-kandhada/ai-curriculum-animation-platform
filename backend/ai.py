import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Create client using key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script(text):
    prompt = f"""
You are an animation script writer.

Convert this story into animation script.

Story:
{text}

Give:
1. Scenes
2. Visual description
3. Narration
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # 🔥 best model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content