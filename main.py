import types

import psycopg2
import telebot

# token
token = '5486877882:AAEK-vc4PvJrrZcsOPHczMwISpmuR3I4RFo'
bot = telebot.TeleBot(token)

conn = psycopg2.connect(
    database="mtucibot_db",
    user="postgres",
    password="92657792Sha_",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


# /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Хочу", "/help", "Расписание по дням недели")
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

# /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\nвыводить расписание на каждый день недели, выводить расписание на текущую неделю, выводить расписание на следующую неделю')


@bot.message_handler(content_types=['text'])
def button_message(message):
    # По дням недели
    if message.text.lower() == 'Расписание по дням недели':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        monday = types.KeyboardButton("Понедельник")
        tuesday = types.KeyboardButton("Вторник")
        wednesday = types.KeyboardButton("среду")
        thursday = types.KeyboardButton("Четверг")
        friday = types.KeyboardButton("Пятница")
        markup.add(monday, tuesday, wednesday, thursday, friday)
        bot.send_message(message.chat.id, 'Выберите день недели', reply_markup=markup)

    # Понедельник
    if message.text.lower() == "понедельник":
        text = f"Расписание на понедельник:\n"
        cursor.execute("SELECT * FROM timetable WHERE day='Понедельник';")
        records = list(cursor.fetchall())
        for i in range(len(records)):
            text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            text += "\n"
        bot.send_message(message.chat.id, text)

    # Вторник
    elif message.text.lower() == "вторник":
        bot.send_message(message.chat.id,f"Расписание на вторник:\n")
        cursor.execute("SELECT * FROM timetable WHERE day='Вторник';")
        records = list(cursor.fetchall())
        text = ''
        for i in range(len(records)):
            text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            text += "\n"
        bot.send_message(message.chat.id, text)
    # Среда
    elif message.text.lower() == "среду":
        text = f"Расписание на среду:\n"
        cursor.execute("SELECT * FROM timetable WHERE day='Среда';")
        records = list(cursor.fetchall())
        for i in range(len(records)):
            text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            text += "\n"
        bot.send_message(message.chat.id, text)
    # Четверг
    elif message.text.lower() == "четверг":
        text = f"Расписание на четверг:\n"
        cursor.execute("SELECT * FROM timetable WHERE day='Четверг';")
        records = list(cursor.fetchall())
        for i in range(len(records)):
            text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            text += "\n"
        bot.send_message(message.chat.id, text)

    # Пятница
    elif message.text.lower() == "пятница":
        text = f"Расписание на пятницу:\n"
        cursor.execute("SELECT * FROM timetable WHERE day='Пятница';")
        records = list(cursor.fetchall())
        for i in range(len(records)):
            text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            text += "\n"
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Я вас не понял")


# Хочу
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда вам сюда - https://mtuci.ru/')



bot.polling(none_stop=True)
