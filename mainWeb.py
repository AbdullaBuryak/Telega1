import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import message
from aiogram.types import Message
from aiogram import F
#from aiogram.dispatcher import command

#from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot("6923436808:AAFGuKqEx_N5DVkiOJNms1WGveT7CZLF644")
dp = Dispatcher()

@dp.message(F.text, Command("start"))

#@dp.message(commands=['start'])
#@dp.message()
# async def message_handler(message: types.Message) -> None:
#     await SendMessage(chat_id=message.from_user.id, text=message.text)

#@dp.message_handler(commands=['start'])
#async def start(message: types.Message):
async def start(message: Message):
    kb = [
        [types.KeyboardButton(text="Open Web Page",web_app=WebAppInfo(url='https://itproger.com'))]
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Hello",reply_markup=keyboard)
    # markup = types.ReplyKeyboardMarkup()
    # markup.add(ty.InlineKeyboardButton('open web page', web_app=WebAppInfo(url='https://itproger.com')))
    # await message.answer("Hello my friend", reply_markup=markup)

async def main():
     await dp.start_polling(bot)

if __name__ == "__main__":
     asyncio.run(main())
dp.start_polling()
#if __name__ == '__main__':
#db.start_polling()