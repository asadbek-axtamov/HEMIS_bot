from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup
import os

TOKEN = os.getenv("TOKEN")

def start(update: Update, context):
    keyboards = [
        ["O'quv reja", "Talaba ma'lumotlari"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboards, resize_keyboard=True)
    update.message.reply_text(
        "Assalomu alaykum. Kerakli bo'limni tanlang:",
        reply_markup=reply_markup
    )

def message_handler(update: Update, context):
    if update.message.text == "O'quv reja":
        keyboard = [
            ['Dars jadvali', 'Davomat'],
            ["O'zlashtirish", "Imtihonlar"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("Kerakli bo'limni tanlang:", reply_markup=reply_markup)

    elif update.message.text == "Talaba ma'lumotlari":
        keyboard = [
            ["Shaxsiy ma'lumotlar", "Rezyume"], 
            ["GPA bali", "Contact number"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("Kerakli bo'limni tanlang:", reply_markup=reply_markup)

    elif update.message.text == "Dars jadvali":
        keyboard = [
            ["Kunlik"], 
            ["Haftalik"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("Kerakli bo'limni tanlang:", reply_markup=reply_markup)

    elif update.message.text == "Davomat":
        keyboard = [
            ["Umumiy"], 
            ["Fanlar bo'yicha"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("Kerakli bo'limni tanlang:", reply_markup=reply_markup)

    elif update.message.text == "Kunlik":
        update.message.reply_text(
            "Dushanba\n09:00 - 09:45 Algoritmlar Ma'ruza\n10:00 - 10:45	Algoritmlar	Amaliy\n11:00 - 11:45	Tarmoq texnologiyalari	Ma'ruza\n13:00 - 13:45	Tarmoq texnologiyalari	Amaliy")

    elif update.message.text == "Haftalik":
        update.message.reply_text(
            "Dushanba\n09:00 - 09:45 Algoritmlar Ma'ruza\n10:00 - 10:45	Algoritmlar	Amaliy\n11:00 - 11:45	Tarmoq texnologiyalari	Ma'ruza\n13:00 - 13:45	Tarmoq texnologiyalari	Amaliy")

    elif update.message.text == "Umumiy":
        update.message.reply_text("jjbjjbjfn")

    elif update.message.text == "Fanlar bo'yicha":
        update.message.reply_text('hghhgghbhnhdfnhdnd')

    elif update.message.text == "O'zlashtirish":
        update.message.reply_text('hghhgghbhnhdfnxnxhdnd')

    elif update.message.text == "Imtihonlar":
        update.message.reply_text('hghhgghbhnhdfnxnxhdnd')

    elif update.message.text == "Shaxsiy ma'lumotlar":
        update.message.reply_text('hghhgghbhnhdfnxnxhdnd')

    elif update.message.text == "Rezyume":
        update.message.reply_text('hghhgghbhnhdfnxnxhdnd')

    elif update.message.text == "GPA bali":
        update.message.reply_text('hghhgghbhnhdfnxnxhdnd')

    elif update.message.text == "Contact number":
        update.message.reply_text('hghhgghbhnhdfnxnxhdnd')




updater = Updater(TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
msg_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(msg_handler)

updater.start_polling()
updater.idle()
