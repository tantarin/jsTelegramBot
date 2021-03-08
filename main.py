from telebot import *
from telebot.types import InlineKeyboardButton, InputMediaPhoto

bot = TeleBot('1670961232:AAGt74keHH_CeyGOi9lxe1FEMNi9-8JBcis')


@bot.message_handler(commands=['start', 'help'])
def send_options(message):
    options = types.InlineKeyboardMarkup()
    options.add(InlineKeyboardButton("Узнать местоположение", callback_data="get_location"),
                               InlineKeyboardButton("Просмотреть номера", callback_data="show_rooms"))
    bot.reply_to(message, 'Выберите один из вариантов', reply_markup=options)


@bot.callback_query_handler(func=lambda call: call.data == 'get_location')
def callback_query_get_location(call):
    bot.send_location(call.message.chat.id, 59.961966, 30.314904)


@bot.callback_query_handler(func=lambda call: call.data == 'show_rooms')
def callback_query_show_rooms(call):
    media = [InputMediaPhoto(open('images/1.jpg', 'rb'), caption="Одноместный номер"), InputMediaPhoto(open('images/2.jpg', 'rb'))]
    bot.send_media_group(call.message.chat.id, media)

# @bot.message_handler()
# def send_welcome(message):
#     print(message)


bot.polling()
