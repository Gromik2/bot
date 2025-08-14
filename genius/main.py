import telebot
from random import randint
from datetime import datetime

TOKEN="8382272036:AAFax0Fo-FTd8thIssUlnNlOJn5JlY1eSl4"
bot=telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id,"Здравствуй человек. Меня зовут genius.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(commands=["date"])
def date(message):
    try:
        bot.send_message(message.chat.id, "Сейчас:"+str(datetime.today()))
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(commands=["random"])
def random(message):
    try:
        bot.send_message(message.chat.id,"Случайное число:."+str(randint(1,1000)))
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(commands=["game"])
def game(message):
    try:
        bot.send_message(message.chat.id, "Сыграй в кости, тебе выпало:" + str(randint(1, 6)))
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(content_types=["text"])
def answer(message):
    try:
        text=message.text

        if text=="Привет":
            bot.send_message(message.chat.id,"Привет!")
        elif text=="Как дела?":
            bot.send_message(message.chat.id, "Отлично")
        elif text == "Как тебя зовут?":
            bot.send_message(message.chat.id, "Меня зовут genius")
        elif text == "Сколько тебе лет?":
            bot.send_message(message.chat.id, "У меня нет возроста")
        else:
            bot.send_message(message.chat.id, text)
    except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка:{e}")


bot.polling(none_stop=True,interval=0)
