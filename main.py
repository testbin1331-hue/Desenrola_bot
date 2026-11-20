import os
import telebot
import google.generativeai as genai

TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Fala! Manda sua dúvida que eu desenrolo pra você 👊")

@bot.message_handler(func=lambda m: True)
def responder(m):
    try:
        resp = model.generate_content(m.text)
        bot.reply_to(m, resp.text)
    except Exception as e:
        bot.reply_to(m, "Deu um erro aqui, tenta de novo!")

print("Bot rodando...")
bot.infinity_polling()
