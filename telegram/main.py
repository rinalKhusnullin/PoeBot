import telebot as tl
import requests

poe_url = "https://2078-83-219-151-30.ngrok-free.app"
autentefication_poe_data = {
  "api_key" : "gkFGqLQUtXQDr2N61nNwU8esV36UMlUI"
}

token = "6207346902:AAEcGfQ4iRaes2w1DRifJo1Yu5ngTGnEOVw"
bot = tl.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  r = requests.post(poe_url, data = {'message':'hi'}) 
  print(r.text)

@bot.message_handler(commands=['start'])
def start_message(message):
  r = requests.post(poe_url, data = {'message':'hi'}) 
  print(r.text)  

bot.infinity_polling()