from openai import OpenAI

client = OpenAI(api_key="AIzaSyA04CSgXUkG2TwilOqg-0jawJzY8UUoH28")

class ModelService:
    async def generate(self, prompt, **kwargs):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content