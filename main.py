import requests
import telebot

from parse_pack.dataPy import Data 
from parse_pack.parse import Parse

from settings.SETTINGS import *

bot = telebot.TeleBot(TOKEN)


def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбери валюту:', reply_markup=create_keyboard().row('Доллар', 'Евро', 'Рубли')) 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    global site, values

    if message.text == 'Доллар':
        site = Parse(URL_USD)
        values = Data(site.get_content())
        bot.send_message(message.chat.id, 'Выберите действие: ', reply_markup=create_keyboard().row('Лучший курс для покупки', 'Вывести полный список', 'Лучший курс для продажи', 'В начало'))
    elif message.text == 'Евро':  
        site = Parse(URL_EUR)
        values = Data(site.get_content())
        bot.send_message(message.chat.id, 'Выберите действие: ', reply_markup=create_keyboard().row('Лучший курс для покупки', 'Вывести полный список', 'Лучший курс для продажи', 'В начало'))
    elif message.text == 'Рубли':  
        site = Parse(URL_RUB)
        values = Data(site.get_content())
        bot.send_message(message.chat.id, 'Выберите действие: ', reply_markup=create_keyboard().row('Лучший курс для покупки', 'Вывести полный список', 'Лучший курс для продажи', 'В начало'))
    elif message.text == 'Лучший курс для покупки':
        bot.send_message(message.chat.id, values.get_best_buy(), reply_markup=create_keyboard().row('Лучший курс для покупки', 'Вывести полный список', 'Лучший курс для продажи', 'В начало'))
    elif message.text == 'Лучший курс для продажи':
        bot.send_message(message.chat.id, values.get_best_sell(), reply_markup=create_keyboard().row('Лучший курс для покупки', 'Вывести полный список', 'Лучший курс для продажи', 'В начало'))
    elif message.text == 'Вывести полный список':
        bot.send_message(message.chat.id, values.get_list(), reply_markup=create_keyboard().row('Лучший курс для покупки', 'Вывести полный список', 'Лучший курс для продажи', 'В начало'))
    elif message.text == 'В начало':
        start_message(message)

    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Напишите /start")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling()