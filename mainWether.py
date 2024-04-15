# Импортируем библиотеку telebot и подмодуль types
import telebot
import requests
import json


# Создаём экземпляр бота с токеном
bot = telebot.TeleBot('6923436808:AAFGuKqEx_N5DVkiOJNms1WGveT7CZLF644')
API = '5fc10db8e820afeefa9730691267c000'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi please write City name:')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'Weather in {city} :{temp}C')
    else:
        bot.reply_to(message, f'Wring City Name. Please try again')

bot.infinity_polling()