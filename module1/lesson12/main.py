from telebot import TeleBot
import requests
from bs4 import BeautifulSoup
import random

token = '5934730511:AAEqrJ35YnyuxHqhP4j6WH3eLSlkLvP05eU'

bot = TeleBot(token=token)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_message(
        message.from_user.id,
        'Привет! Я бот-помощник. Список команд :\n/parse - парсинг сайта\n/random - игра угадай число'
        )

@bot.message_handler(commands=['parse'])
def facts_parse(message):
    respons = requests.get('https://i-fakt.ru')
    soup = BeautifulSoup(respons.text,'html.parser')
    facts = soup.find_all(class_='p-2 clearfix')
    random_fact = random.choice(facts)
    text = random_fact.h4.text + '\n' + random_fact.a['href']
    bot.send_message(message.from_user.id, text)


bot.polling()

