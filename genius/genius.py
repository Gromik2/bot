import telebot
from random import randint
from datetime import datetime

TOKEN = "8382272036:AAFax0Fo-FTd8thIssUlnNlOJn5JlY1eSl4"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = telebot.types.KeyboardButton(text="Игра в кубик")
        button2 = telebot.types.KeyboardButton(text="Игровой автомат")
        keyboard.add(button1, button2)
        bot.send_message(message.chat.id, "Здравствуй человек. Меня зовут genius.", reply_markup=keyboard)
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
        bot.send_message(message.chat.id, "Случайное число:."+str(randint(1, 1000)))
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(commands=['image'])
def send_image(message):
    try:
        file = open("ежик.jpg", 'rb')
        bot.send_photo(message.chat.id, file, caption="Изображение ежа:")
        file.close()
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(commands=['image1'])
def send_image(message):
    try:
        file = open("Rectangle 23.png", 'rb')
        bot.send_photo(message.chat.id, file, caption="Изображение еды:")
        file.close()
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(commands=['image2'])
def send_image(message):
    try:
        file = open("scale_1200.jpeg", 'rb')
        bot.send_photo(message.chat.id, file, caption="Изображение природы:")
        file.close()
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(commands=['about'])
def information(message):
    try:
        bot.send_message(message.chat.id, "Я бот который знает все, но пока что я в стадии разработки")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.message_handler(content_types=["text"])
def answer(message):
    try:
        text = message.text

        if text == "Привет":
            bot.send_message(message.chat.id, "Привет!")
        elif text == "Как дела?":
            bot.send_message(message.chat.id, "Отлично")
        elif text == "Какая твоя любимая игра на пк?":
            bot.send_message(message.chat.id, "Roblox")
        elif text == "Какое у тебя любимое блюдо":
            bot.send_message(message.chat.id, "Я не нуждаюсь в еде")
        elif text == "Как тебя зовут?":
            bot.send_message(message.chat.id, "Меня зовут genius")
        elif text == "Сколько тебе лет?":
            bot.send_message(message.chat.id, "У меня нет возроста")
        elif text == "Игровой автомат":
            value = bot.send_dice(message.chat.id, emoji='🎰').dice.value
            if value in (1, 16, 22, 32, 43, 48):
                bot.send_message(message.chat.id, "Победа!")
            elif value == 64:
                bot.send_message(message.chat.id, "Jackpot!")
            else:
                bot.send_message(message.chat.id, "Попробуй еще раз")
        elif text == "Игра в кубик":
            keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=3)
            button1 = telebot.types.InlineKeyboardButton("1", callback_data='1')
            button2 = telebot.types.InlineKeyboardButton("2", callback_data='2')
            button3 = telebot.types.InlineKeyboardButton("3", callback_data='3')
            button4 = telebot.types.InlineKeyboardButton("4", callback_data='4')
            button5 = telebot.types.InlineKeyboardButton("5", callback_data='5')
            button6 = telebot.types.InlineKeyboardButton("6", callback_data='6')
            keyboard2.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(message.chat.id, "Угадай число на кубике", reply_markup=keyboard2)
        else:
            bot.send_message(message.chat.id, text)
    except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка:{e}")


@bot.callback_query_handler(func=lambda call: call.data in ('1', '2', '3', '4', '5', '6'))
def dice_answer(call):
    value = bot.send_dice(call.message.chat.id, emoji='').dice.value
    if str(value) == call.data:
        bot.send_message(call.message.chat.id, "Победа")
    else:
        bot.send_message(call.message.chat.id, "Попробуй еще раз")


bot.polling(none_stop=True, interval=0)
