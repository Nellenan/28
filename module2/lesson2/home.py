from telebot import TeleBot
from telebot.types import (Message,
                           ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)
import random

bot = TeleBot('5934730511:AAEqrJ35YnyuxHqhP4j6WH3eLSlkLvP05eU')
BASE_FILES_DIR = r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module2\lesson2\extra'

def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button1 = KeyboardButton('/cats')
    button2 = KeyboardButton('/poem')
    button3 = KeyboardButton('/sticker')
    button4 = KeyboardButton('/music')
    button5 = KeyboardButton('/random_game')
    button6 = KeyboardButton('/game_genre')

    keyboard.add(button1, button2, button3, button4, button5, button6)
    return keyboard


@bot.message_handler(commands=['start', 'help'])
def welcome(message: Message):
    keyboard = welcome_keyboard()
    bot.send_message(message.from_user.id, 'Привет! Выдбери следующие команды:', reply_markup=keyboard)


@bot.message_handler(commands=['cats'])
def cats(message: Message):
    random_img_number = random.randint(1, 9)
    random_img = open(fr'{BASE_FILES_DIR}\{random_img_number}.jpg', 'rb')
    bot.send_photo(message.from_user.id, random_img)


@bot.message_handler(commands=['music'])
def music(message: Message):
    audio = open(fr'{BASE_FILES_DIR}\happy.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)

@bot.message_handler(commands=['poem'])
def poem(message: Message):
    bot.send_message(message.from_user.id, 'Села муха на варенье, вот и всё стихотворение! ')
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text='Перейти', url="https://stihi.ru")
    keyboard.add(button)

    bot.send_message(message.from_user.id, 'Больше стихотворений здесь:', reply_markup=keyboard)

@bot.message_handler(commands=['sticker'])
def sticker(message: Message):
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEG-CljpcxTtdbxQ-m014MilUl3D3tTKwACKSgAAoPcMEmIESVJ7yHFVSwE')

@bot.message_handler(commands=['random_game'])
def random_game(message: Message):
    games = ['CSGO', 'Dark Souls', 'PUBG', 'Dying Light']
    game = random.choice(games)
    bot.send_message(message.from_user.id, game)

@bot.message_handler(commands=['game_genre'])
def genre(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text='Шутер', url='https://www.ubisoft.com/ru-ru/game/far-cry/far-cry-3')
    button2 = InlineKeyboardButton(text='Королевская битва', url='https://store.epicgames.com/ru/p/pubg-59c1d9')
    button3 = InlineKeyboardButton(text='Слэшер', url='https://www.playstation.com/en-us/games/devil-may-cry-5/')
    keyboard.add(button1, button2, button3)

    bot.send_message(message.from_user.id, 'Выбери жанр игры:', reply_markup=keyboard)



bot.polling()






