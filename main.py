import telebot

TOKEN = 8500336089:AAFv0ddfeiOMH0OlTRvjd4CFKmUprkHMz74

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Bot ishlayapti 🚀")

bot.polling()
