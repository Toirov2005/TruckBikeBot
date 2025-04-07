import os
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

blocked_words = ["спам", "ссылка", "лохотрон"]

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_message(msg: Message):
    text = msg.text.lower()

    if any(word in text for word in blocked_words):
        await msg.delete()
        return

    if "цена" in text or "сколько стоит" in text:
        await msg.answer("Здравствуйте, слушаю вас, чем могу помочь? Уточните, пожалуйста, модель?")
    elif "доставка" in text:
        await msg.answer("Доставка бесплатная в день заказа! Уточните город и модель?")
    else:
        await msg.answer("Здравствуйте, слушаю вас, чем могу помочь?")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
