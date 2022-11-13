import psycopg2
import telebot
from telebot import types
import datetime
from random import randint

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
weekInfo = ''

if (wek % 2) == 0:
    weekInfo = 'четная'
else:
    weekInfo = 'нечетная'


# /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Хочу", "/help", "Расписание по днями", "/week", "/nextweek", "/game")
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


# /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу: \nвыводить расписание на каждый день недели, \nвыводить расписание на текущую неделю /week, \nвыводить расписание на следующую неделю /nextweek, \nсыграть с вами в игру /game')


# This week
@bot.message_handler(commands=['week'])
def week(message):
    parity = ''
    if weekInfo == 'нечетная':
        parity = 'timetable_odd'
    elif weekInfo == 'четная':
        parity = 'timetable_even'

    # Понедельник
    monday = '\n Понедельник:\n'
    cursor.execute(f"SELECT * FROM {parity} WHERE day='Понедельник';")
    records = list(cursor.fetchall())

    if len(records) == 0:
        monday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            monday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            monday += "\n"

    # Вторник
    tuesday = 'Вторник:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Вторник';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        tuesday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            tuesday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            tuesday += "\n"

    # Среда
    wednesday = 'Среда:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Среда';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        wednesday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            wednesday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            wednesday += "\n"

    # Четверг
    thurs = 'Четверг:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Четверг';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        thurs += '<Занятий нет>\n \n'
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
        friday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            friday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            friday += "\n"

    # Суббота
    saturday = 'Cуббота:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Суббота';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        saturday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            saturday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            saturday += "\n"

    bot.send_message(message.chat.id,
                     'Расписание на текущую неделю\n' + weekInfo + monday + tuesday + wednesday + thurs + friday + saturday)


# Next week
@bot.message_handler(commands=['nextweek'])
def week(message):
    parity = ''
    if weekInfo == 'нечетная':
        parity = 'timetable_even'
    elif weekInfo == 'четная':
        parity = 'timetable_odd'

    # Понедельник
    monday = '\n Понедельник:\n'
    cursor.execute(f"SELECT * FROM {parity} WHERE day='Понедельник';")
    records = list(cursor.fetchall())

    if len(records) == 0:
        monday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            monday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            monday += "\n"

    # Вторник
    tuesday = 'Вторник:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Вторник';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        tuesday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            tuesday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            tuesday += "\n"

    # Среда
    wednesday = 'Среда:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Среда';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        wednesday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            wednesday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            wednesday += "\n"

    # Четверг
    thurs = 'Четверг:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Четверг';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        thurs += '<Занятий нет>\n \n'
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
        friday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            friday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            friday += "\n"

    # Суббота
    saturday = 'Cуббота:\n'
    cursor.execute("SELECT * FROM timetable_odd WHERE day='Суббота';")
    records = list(cursor.fetchall())
    if len(records) == 0:
        saturday += '<Занятий нет>\n \n'
    else:
        for i in range(len(records)):
            saturday += f"<{records[i][2]}> <{records[i][3]}> <{records[i][4]}> \n"
            saturday += "\n"

    bot.send_message(message.chat.id,
                     'Расписание на следующу ю неделю\n' + weekInfo + monday + tuesday + wednesday + thurs + friday + saturday)


@bot.message_handler(commands=['game'])
def random(message):
    comp = randint(1, 100)
    user = randint(1, 100)
    if comp > user:
        bot.send_message(message.chat.id, f'Бот выиграл\n У вас: {user}\n У бота: {comp} ')
    elif comp == user:
        bot.send_message(message.chat.id, f'\n У вас: {user}\n У бота: {comp}')
    else:
        bot.send_message(message.chat.id, f'Вы выиграл\n У вас: {user}\n У бота: {comp} ')


# Schedule by day
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

#
# # Хочу
# @bot.message_handler(content_types=['text'])
# def answer(message):
#     if message.text.lower() == "хочу":
#         bot.send_message(message.chat.id, 'Тогда вам сюда - https://mtuci.ru/')


bot.polling(none_stop=True)
