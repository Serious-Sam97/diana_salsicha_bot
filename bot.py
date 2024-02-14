import telebot
from dotenv import load_dotenv
import os
from openai import OpenAI
import openai

load_dotenv();
bot = telebot.TeleBot(os.getenv('TELEBOT_API_KEY'));
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

assistant_id = os.getenv('OPENAI_ASSISTANT_KEY');

def send_message_openai(message):
    response = client.chat.completions.create(
    	model="gpt-3.5-turbo",
    	messages=[{"role": "user", "content": message}],
	);
    return response.choices[0].message.content;

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ahoy Sir, how can I help?");
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    apiMessage = send_message_openai(message.text);
    bot.reply_to(message, apiMessage);
bot.infinity_polling()
