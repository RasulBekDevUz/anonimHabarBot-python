import sqlite3
import telebot
from telebot.types import *
from telebot import types
bot = telebot.TeleBot("6180944786:AAF4lgf0cq0YqXUOQxaFC7Itgxu0VCT1gNA")


@bot.message_handler(commands=['start'])
def send_inline(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    settings_button = types.InlineKeyboardButton(text='Devloper 👨‍💻', url='https://t.me/pythonDevIoper')
    help_button = types.InlineKeyboardButton(text='👥 add ➕', url='https://t.me/AnonimButonMessageBot?startgroup=true')
    keyboard.add(settings_button, help_button)
    bot.send_message(message.chat.id, 'Asalomu aleykum 👋🏻\nAnonim 👻 message 💬 \nBot🤖 ga Hush☺️ kelibsiz 🚶\nFunk dan foydalanish uchun Inline dan foydalaning\n\n@AnonimButonmessageBot', reply_markup=keyboard)

dic = {}
@bot.inline_handler(func=lambda call:True)
def custom(call):
    if '|' in call.query:
        try:
            user = "@"+str(call.query).split("|")[0]
            user1 = str(call.query).split("|")[0]
            key = InlineKeyboardMarkup().add(InlineKeyboardButton(text=" O'qish 🔍",callback_data=f"user-{user1}"))
            answer = InlineQueryResultArticle(call.id,"🔥 Anonim Habar",InputTextMessageContent(message_text=f"👻 Anonim Habar 💬 {user} Uchun 🌚 ",parse_mode='html'),reply_markup=key)
            dic[user1]=str(call.query).split("|")[1]
            bot.answer_inline_query(call.id,[answer])
        except:
            pass
@bot.callback_query_handler(func=lambda call:True)
def callhancler(call):
    if 'user-' in call.data:
        try:
            user = str(call.data).split("user-")[1]
            if (str(call.from_user.username)) =='None':
                bot.answer_callback_query(call.id,text="Bu habar 💬 sen uchun yozil ✍ magan 🙅‍♂ Devloper >>> Rasul",show_alert=True)
            elif user in call.from_user.username:
                bot.answer_callback_query(call.id,text=dic[user],show_alert=True)
            else:
                bot.answer_callback_query(call.id,text="Bu habar 💬 sen uchun yozil ✍ magan 🙅‍♂ Devloper >>> Rasul",show_alert=True)
        except:
            bot.answer_callback_query(call.id,text="Bu habar 💬 eskirgan 🗑",show_alert=True)
bot.infinity_polling()