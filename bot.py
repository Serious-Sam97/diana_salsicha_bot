import telebot
from dotenv import load_dotenv
import os
from openai import OpenAI
import openai
import time

load_dotenv();
bot = telebot.TeleBot(os.getenv('TELEBOT_API_KEY'));
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

assistant_id = os.getenv('OPENAI_ASSISTANT_KEY');
thread = client.beta.threads.create()

def send_message_openai(prompt):
   client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    );
   run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        instructions="Its our dog diana, its angry but funny too, speaks dog language but the translation is on PTBR"
    );
   while run.status != "completed":
       time.sleep(0.5);
       run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
   messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

   return messages.data[0].content[0].text.value;

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ahoy Sir, how can I help?");
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    apiMessage = send_message_openai(message.text);
    finalMessage = apiMessage if apiMessage else "Nada a declarar!";
    bot.reply_to(message, finalMessage);
bot.infinity_polling()
