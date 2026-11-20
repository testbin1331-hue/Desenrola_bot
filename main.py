import os
import telebot
import google.generativeai as genai

TOKEN = os.environ.get("TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
modelo = genai.GenerativeModel("gemini-2.5-flash")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def comecar(m):
    bot.reply_to(m, "Fala! Manda sua pergunta que eu desenrolo pra você.")

@bot.message_handler(func=lambda m: True)
def responder(m):
    try:
        resposta = modelo.generate_content(m.text)
        bot.reply_to(m, resposta.text)
    except Exception as e:
        bot.reply_to(m, f"Deu erro aqui: {e}")

bot.polling()
