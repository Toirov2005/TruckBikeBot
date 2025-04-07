import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Ты помощник магазина электровелосипедов TruckBike. Отвечай уверенно, по делу, с лёгким продающим стилем."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Произошла ошибка при обращении к ИИ: {e}"
