import telebot

bot = telebot.TeleBot("6741867245:AAFZxpRbhRrteB-KiOVAWaXU3C32JnCvqc0");

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Ahoy Sir, how can I help?");

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# bot.reply_to(message, message.text)
	bot.reply_to(message, "WHAAAAT")

bot.infinity_polling()
