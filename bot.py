import telebot
import openai
from dotenv import load_dotenv
import os

load_dotenv();

openai.api_key = os.getenv('OPENAI_API_KEY');
bot = telebot.TeleBot(os.getenv('TELEBOT_API_KEY'));

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ahoy Sir, how can I help?");
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # bot.reply_to(message, message.text)
    bot.reply_to(message, "WHAAAAT")
bot.infinity_polling()