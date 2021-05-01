from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import requests

updater = Updater(token='1761265222:AAH5msiomTt6ML2q_LL3nzmwnw7GaMH34AM', use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Напиши мне совй город и я скажу тебе погоду")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def weather(update, context):
    city = update.message.text
    w = requests.get(f'https://wttr.in/{city}?format=3')
    context.bot.send_message(chat_id=update.effective_chat.id, text=w.text)


weather_handler = MessageHandler(Filters.text & (~Filters.command), weather)
dispatcher.add_handler(weather_handler)
updater.start_polling()
updater.idle()