#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from tocken import tocken


bot = telebot.TeleBot(tocken)

@bot.message_handler(commands=["start"])
def starting_message(message):
    bot.send_message(message.chat.id, "Hello! To find out the sticker ID, send me any sticker")

@bot.message_handler(content_types=["sticker"])
def get_sticker_id(message):
    bot.send_message(message.chat.id, message.sticker.file_id)

@bot.message_handler(content_types=["text"])
def bot_sending_sticker(message):
    bot.send_sticker(message.chat.id, message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)
