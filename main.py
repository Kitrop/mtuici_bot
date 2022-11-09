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
    keyboard.row("Хочу", "/help", "Расписание по дням недели")
    bot.send_message(message.chat.id, 'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


# /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:'
                                      '\nвыводить расписание на каждый день недели, выводить расписание на текущую неделю, выводить расписание на следующую неделю')


@bot.message_handler(commands=['week'])
def week(message):
    cursor.execute("SELECT * FROM timetable_odd")
    records = list(cursor.fetchall())

    text = ''
    mondayCount = 0
    monday = f'=======================\n Понедельник:\n'

    tuesdayCount = 0
    tuesday = f'=======================\n Вторник:\n'

    wednesdayCount = 0
    wednesday = f'=======================\n Среда:\n'

    thursCount = 0
    thurs = f'=======================\n Четверг:\n'

    fridayCount = 0
    friday = f'=======================\n Пятница:\n'

    saturdayCount = 0
    saturday = f'=======================\n Суббота:\n'

    for i in range(len(records)):
        if records[i][1] == 'Понедельник':
            mondayCount += 1
        if records[i][1] == 'Вторник':
            tuesdayCount += 1
        if records[i][1] == 'Среда':
            wednesdayCount += 1
        if records[i][1] == 'Четверг':
            thursCount += 1
        if records[i][1] == 'Пятница':
            fridayCount += 1
        if records[i][1] == 'Суббота':
            saturdayCount += 1
    for j in range(mondayCount):
        monday += f' <{records[j][2]}> <{records[j][3]}> <{records[j][4]}> \n '
    for k in range(tuesdayCount):
        tuesday += f' <{records[k][2]}> <{records[k][3]}> <{records[k][4]}> \n '
    for c in range(wednesdayCount):
        wednesday += f' <{records[c][2]}> <{records[c][3]}> <{records[c][4]}> \n '
    for v in range(thursCount):
        thurs += f' <{records[v][2]}> <{records[v][3]}> <{records[v][4]}> \n '
    for b in range(fridayCount):
        friday += f' <{records[b][2]}> <{records[b][3]}> <{records[b][4]}> \n '
    for n in range(saturdayCount):
        saturday += f' <{records[n][2]}> <{records[n][3]}> <{records[n][4]}> \n '

    bot.send_message(message.chat.id, monday + tuesday + wednesday + thurs + friday + saturday)

    # 1 - день
    # 2 - предмет
    # 3 - кабинет
    # 4 - время


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
