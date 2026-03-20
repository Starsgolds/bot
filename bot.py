import time
from telegram import Bot
from parser import start_parser
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def send_results():
    items = start_parser()

    if not items:
        bot.send_message(chat_id=CHAT_ID, text="Ничего не найдено 😢")
        return

    for item in items:
        text = f"""
📦 {item['name']}
💰 Цена: {item['price']} ₽
🎁 Баллы: {item['bonus']}
📊 Выгода: {item['percent']}%
🔗 {item['link']}
"""
        bot.send_message(chat_id=CHAT_ID, text=text)


if __name__ == "__main__":
    while True:
        send_results()
        time.sleep(1800)  # каждые 30 минут
