# Импортируем необходимые библиотеки
import telebot
import webbrowser

# Закомментирована строка импорта requests и соответствующие переменные, так как они не используются в данном коде
# import requests
# proxies = {
#     'http': 'http://localhost:8080',
#     'https': 'https://localhost:8080',

# }
# url = "https://api.telegram.org"
# out = requests.get(url, proxies=proxies).text

# Создаем экземпляр бота TeleBot с вашим токеном
bot = telebot.TeleBot("6923436808:AAFGuKqEx_N5DVkiOJNms1WGveT7CZLF644")

# Определяем функцию обработки команд /site и /website, которая открывает веб-сайт в браузере
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')

# Определяем функцию обработки команды /start, которая приветствует пользователя
@bot.message_handler(commands=['start'])
def main(message):
    #bot.send_message(message.chat.id, message)  # Комментарий: Эта строка закоментирована, так как она не делает ничего полезного
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name} {message.from_user.last_name}')

# Определяем функцию обработки команды /hello, которая отвечает на приветствие пользователя
@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, 'Hello  Guncha')

# Определяем функцию обработки команды /info, которая отправляет информацию о себе
@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, '<b>Hello</b> <em><u>Information</u></em>', parse_mode='html')

# Определяем функцию обработки сообщений, которые не являются командами
@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')

    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')

# Запускаем бота на постоянное ожидание сообщений
bot.polling(non_stop=True)