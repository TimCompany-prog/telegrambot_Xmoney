import telebot
import requests
from time import time#message_chat_id = t.me/novinikkas8B
bot = telebot.TeleBot('1027784495:AAFoTJzFPw8w4lucoAD-FzrHgeaOg3pURMI')

from telebot import types
a = types.ReplyKeyboardMarkup(resize_keyboard=True)
a1 = types.KeyboardButton("заработать🏧")
a2 = types.KeyboardButton("вывод💳")
a3 = types.KeyboardButton("разработчик👨‍💻")
a4 = types.KeyboardButton("чат📝")
a.add(a1,a2,a3,a4)
ab = types.InlineKeyboardMarkup()
a5 = types.InlineKeyboardButton(text="чат📝",url='https://t.me/chatpeo')
ab.add(a5)
af = types.InlineKeyboardMarkup(row_width=2)
a6 = types.InlineKeyboardButton(text="посмотреть рекламу",callback_data='as')
a7 = types.InlineKeyboardButton(text="подписаться на канал",url='https://t.me/chatpeo')
af.add(a6,a7)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот, узнать команды - /help',reply_markup=a)
@bot.message_handler(commands=['help'])
def start_message(message):

    bot.send_message(message.chat.id, '')

@bot.message_handler(content_types=['text'])
def send_text(message):

     bot.send_message(-1001199377093,message.text)



     if message.text.lower() == 'вывод💳':

        bot.send_message(message.chat.id, 'У тебя 0, но скоро будет 10000$')
     if message.text.lower() == 'заработать🏧':
        bot.send_message(message.chat.id,"Способы заработать🏧",reply_markup=af)

        
        #bot.restrict_chat_member(-1001461255585,, until_date=time()+120)
        #bot.send_message(-1001485207430, "привіт всім")
        #bot.send_message(-1001461255585, "привіт сімʼя")
     if message.text.lower() == 'разработчик👨‍💻':
        bot.send_message(message.chat.id, 'Мой разработчик @timproger')
     if message.text.lower() == 'чат📝':
        
         bot.send_message(message.chat.id,'Сcылка на групу',reply_markup=ab)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'as':
                bot.send_message(call.message.chat.id, 'зарегистрируйся и смотри рекламу\nhttps://globus-inter.com/uk/land/people?invite=7671830')
    except Exception as e:
        
        print(repr(e))



bot.polling(none_stop=True)
