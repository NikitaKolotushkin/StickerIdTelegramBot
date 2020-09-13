#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from tocken import tocken


bot = telebot.TeleBot(tocken)

@bot.message_handler(commands=["start"])
def starting_message(message):
    bot.send_message(message.chat.id, "Hi, you write /start command!")

if __name__ == "__main__":
    bot.polling(none_stop=True)
