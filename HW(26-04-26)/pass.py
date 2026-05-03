import telebot
import os
import random
import string
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("Токен не найден")
    exit()

bot = telebot.TeleBot(TOKEN)

# символы для пароля
symbols = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Отправь длину пароля и я его сгенерирую"
    )

def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(symbols)
    return password

@bot.message_handler(content_types=['text'])
def handler(message):
    text = message.text

    if text.isdigit():
        length = int(text)

        if length < 4:
            bot.send_message(message.chat.id, "Слишком короткий пароль")
            return

        if length > 50:
            bot.send_message(message.chat.id, "Слишком длинный пароль")
            return

        password = generate_password(length)

        bot.send_message(
            message.chat.id,
            f"пароль:\n{password}"
        )
    else:
        bot.send_message(
            message.chat.id,
            "Отправьте длину"
        )

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()