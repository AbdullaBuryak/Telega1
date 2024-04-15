import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6923436808:AAFGuKqEx_N5DVkiOJNms1WGveT7CZLF644')

currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi enter a sum')
    bot.register_next_step_handler(message, summ)

def summ(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Enter correct Sum')
        bot.register_next_step_handler(message, summ)
        return

    if amount > 0:

        markup = types.InlineKeyboardMarkup(row_width =2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data = 'usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data = 'eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data = 'usd/gbp')
        btn4 = types.InlineKeyboardButton('other', callback_data = 'else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'choose other pair', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Sum must be grater than 0')
        bot.register_next_step_handler(message, summ)

@bot.callback_query_handler(func=lambda  call:True)
def callback(call):
    
    if call.data != 'else':
        values= call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Pjluchitsya: {round(res, 2)}. You can try again')
        bot.register_next_step_handler(call.message, summ)
    else:
        bot.send_message(call.message.chat.id, 'Enter a pair')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        values= message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Poluchitsya: {round(res, 2)}. You can try again')
        bot.register_next_step_handler(message, summ)
    except Exception:
        bot.send_message(message.chat.id, 'Some think wrong try again')
        bot.register_next_step_handler(message, my_currency)
 
bot.infinity_polling()