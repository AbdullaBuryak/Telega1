# Импортируем библиотеку telebot и подмодуль types
import telebot
from telebot import types

# Создаём экземпляр бота с токеном
bot = telebot.TeleBot('6923436808:AAFGuKqEx_N5DVkiOJNms1WGveT7CZLF644')

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создаём клавиатуру для ответа
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(text='Go to Site')
    markup.row(btn1)
    btn2 = types.KeyboardButton(text='Delete Photo')
    btn3 = types.KeyboardButton(text='Edite Text')
    markup.row(btn2, btn3)
    
    # Отправляем фотографию с вложенной клавиатурой
    with open('./photo.png', 'rb') as file:
        bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    
    # Регистрируем следующий шаг обработки сообщения
    bot.register_next_step_handler(message, onclick)

# Обработка нажатия кнопок в клавиатуре
def onclick(message):
    if message.text == 'Go to Site':
        bot.send_message(message.chat.id, 'Web is open')
    elif message.text == 'Delete Photo':
        bot.send_message(message.chat.id, 'Deleted')

# Обработка контента сообщений
@bot.message_handler(content_types=['photo', 'audio'])
def get_photo(message):
    # Создаём клавиатуру для ответа
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Go to Site', url='https://itproger.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text='Delete Photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton(text='Edite Text', callback_data='edit')
    markup.row(btn2, btn3)
    
    # Отвечаем на сообщение с вложенной клавиатурой
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)

# Обработка callback-сообщений
@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

# Запуск бесконечного опрос
bot.infinity_polling()