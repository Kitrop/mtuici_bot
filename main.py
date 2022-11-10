import psycopg2
import telebot
from telebot import types
import datetime

# token
token = '5486877882:AAEK-vc4PvJrrZcsOPHczMwISpmuR3I4RFo'
bot = telebot.TeleBot(token)

conn = psycopg2.connect(
    database="mtucibot_db",
    user="postgres",
    password="9265",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

#
date = datetime.datetime.now()
dt = datetime.date(date.year, date.month, date.day)
wek = dt.isocalendar()[1]
week = ''

if (wek % 2) == 0:
    week = 'нижняя'
else:
    week = 'верхняя'


# /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Хочу", "/help", "Расписание по дням недели", "/week")
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


# /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу:'
                                      '\nвыводить расписание на каждый день недели, '
                                      '\nвыводить расписание на текущую неделю /week,'
                                      '\nвыводить расписание на следующую неделю /nextweek',)

# This week
@bot.message_handler(commands=['week'])
def week(message):
    # Понедельник
    monday = 'Понедельник:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Понедельник';")
    records = list(cursor.fetchall())

    if len(records) == 0:
        bot.send_message(message.chat.id, monday + '<Занятий нет>')
    else:
        for i in range(len(records)):
            monday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            monday += "\n"

    # Вторник
    tuesday = 'Вторник:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Вторник';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        bot.send_message(message.chat.id, tuesday + '<Занятий нет>')
    else:
        for i in range(len(records)):
            tuesday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            tuesday += "\n"

    # Среда
    wednesday = 'Среда:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Среда';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        bot.send_message(message.chat.id, wednesday + '<Занятий нет>')
    else:
        for i in range(len(records)):
            wednesday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            wednesday += "\n"

    # Четверг
    thurs = 'Четверг:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Четверг';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        bot.send_message(message.chat.id, thurs + '<Занятий нет>')
    else:
        for i in range(len(records)):
            thurs += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            thurs += "\n"

    # Пятница
    friday = 'Пятница:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Пятница';")
    records = list(cursor.fetchall())
    print(len(records))
    if len(records) == 0 or not records:
        print('len 0')
        bot.send_message(message.chat.id, friday + '<Занятий нет>')
    else:
        for i in range(len(records)):
            friday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            friday += "\n"

    # Суббота
    saturday = 'Cуббота:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Суббота';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        bot.send_message(message.chat.id, saturday + '<Занятий нет>')
    else:
        for i in range(len(records)):
            saturday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            saturday += "\n"

    bot.send_message(message.chat.id, monday + tuesday + wednesday + thurs + friday + saturday)


@bot.message_handler(content_types=['text'])
def day(message):
    if message.text.lower() == "расписание по дням":
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
        cursor.execute("SELECT * FROM timetable_odd WHERE day='Понедельник';")
        records = list(cursor.fetchall())

        if len(records) == 0:
            bot.send_message(message.chat.id, text + '<Занятий нет>')
        else:
            for i in range(len(records)):
                text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
                text += "\n"
            bot.send_message(message.chat.id, text)


    # Вторник
    elif message.text.lower() == "вторник":
        text = f"Расписание на вторник:\n"
        cursor.execute("SELECT * FROM timetable_odd WHERE day='Вторник';")
        records = list(cursor.fetchall())

        if len(records) == 0:
            bot.send_message(message.chat.id, text + '<Занятий нет>')
        else:
            for i in range(len(records)):
                text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
                text += "\n"
            bot.send_message(message.chat.id, text)

    # Среда
    elif message.text.lower() == "среду":
        text = f"Расписание на среду:\n"
        cursor.execute("SELECT * FROM timetable_odd WHERE day='Среда';")
        records = list(cursor.fetchall())

        if len(records) == 0:
            bot.send_message(message.chat.id, text + '<Занятий нет>')
        else:
            for i in range(len(records)):
                text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
                text += "\n"
            bot.send_message(message.chat.id, text)

    # Четверг
    elif message.text.lower() == "четверг":
        text = f"Расписание на четверг:\n"
        cursor.execute("SELECT * FROM timetable_odd WHERE day='Четверг';")
        records = list(cursor.fetchall())
        if len(records) == 0:
            bot.send_message(message.chat.id, text + '<Занятий нет>')
        else:
            for i in range(len(records)):
                text += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
                text += "\n"
            bot.send_message(message.chat.id, text)

    # Пятница
    elif message.text.lower() == "пятница":
        text = f"Расписание на пятницу:\n"
        cursor.execute("SELECT * FROM timetable_odd WHERE day='Пятница';")
        records = list(cursor.fetchall())
        if len(records) == 0:
            bot.send_message(message.chat.id, text + '<Занятий нет>')
        else:
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
