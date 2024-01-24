import telebot;
from telebot import types
bot = telebot.TeleBot('6927121969:AAGMmTfRqdOHSmnqdpNnIL-4Pe6GuLNyV_Y')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "Как дела":
        bot.send_message(message.from_user.id, "Хорошо а у тебя ?")    
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)