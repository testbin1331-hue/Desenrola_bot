import os
import threading
import telebot
import google.generativeai as genai
from flask import Flask

TOKEN = os.environ.get("TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
modelo = genai.GenerativeModel("gemini-3.8-flash")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot online!"

@bot.message_handler(commands=["start"])
def comecar(m):
    bot.reply_to(m, "Fala! Manda sua pergunta que eu respondo!")

@bot.message_handler(func=lambda m: True)
def responder(m):
    try:
        resposta = modelo.generate_content(m.text)
        bot.reply_to(m, resposta.text)
    except Exception as e:
        bot.reply_to(m, f"Deu erro aqui: {e}")

def rodar_bot():
    bot.polling()

if __name__ == "__main__":
    threading.Thread(target=rodar_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
