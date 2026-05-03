import telebot
import os
import random
from dotenv import load_dotenv
from telebot import types

load_dotenv()

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    print("Токен не найден")
    exit()

bot = telebot.TeleBot(TOKEN)


menu_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_play = types.KeyboardButton('Играть')
menu_kb.add(btn_play)


game_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_rock = types.KeyboardButton('Камень')
btn_paper = types.KeyboardButton('Бумага')
btn_scissors = types.KeyboardButton('Ножницы')
game_kb.add(btn_rock, btn_paper, btn_scissors)

def bot_choice():
    return random.choice(['Камень', 'Бумага', 'Ножницы'])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Это бот Камень-Ножницы-Бумага.\nНажми 'Играть' чтобы начать.",
        reply_markup=menu_kb
    )

@bot.message_handler(func=lambda message: message.text == 'Играть')
def play(message):
    bot.send_message(
        message.chat.id,
        "Выбери: Камень, Бумага или Ножницы",
        reply_markup=game_kb
    )

@bot.message_handler(func=lambda message: message.text in ['Камень', 'Бумага', 'Ножницы'])
def game(message):
    user = message.text
    comp = bot_choice()

    if user == comp:
        result = "Ничья"
    elif (user == 'Камень' and comp == 'Ножницы') or \
         (user == 'Бумага' and comp == 'Камень') or \
         (user == 'Ножницы' and comp == 'Бумага'):
        result = "Ты"
    else:
        result = "я"

    bot.send_message(
        message.chat.id,
        f"Ты: {user}\nБот: {comp}\nВыйграл: {result}",
        reply_markup=menu_kb
    )

exit_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
exit_kb.add(types.KeyboardButton('Выход'))

@bot.message_handler(func=lambda message: message.text == 'Выход')
def exit_game(message):
    bot.send_message(
        message.chat.id,
        "Игра закончилась",
        reply_markup=menu_kb
    )

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()