from telegram import Update
from telegram.ext import ContextTypes
import json

async def check_blacklist(message):
    with open("blacklist.json", "r", encoding="utf-8") as file:
        banned = json.load(file)["banned_words"]
    return any(word.lower() in message.lower() for word in banned)

async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здравствуйте, слушаю вас, чем могу помочь?")

async def support_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Служба поддержки 24/7 на связи! Задайте свой вопрос.")
