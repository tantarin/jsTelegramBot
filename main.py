import telebot

bot = telebot.TeleBot('<<token>>')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print()
    bot.reply_to(message, f'Дороу {message.from_user.first_name or message.from_user.username or "Hi"}')


bot.polling()
