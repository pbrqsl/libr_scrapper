import telebot
import analyzer
import re
from telebot import TeleBot
import telebot
import utils._sec

bot= telebot.TeleBot(utils._sec.bot_test_API)
ids_dict = {
    'r': '4394568',
    'm': '6186174'
}

menu = """
m - martyna
r - rafal
srcr - srednia calkowita rafal
srm - srednie czastkowe martynka
orbiol - oceny rafal biologia
omprzy30 - oceny martyna geografia ost. 30 dni
or - oceny rafal z ost. 7 dni
"""

@bot.message_handler (commands=['BotCommands'])
def BotCommands (message):
    bot.reply_to(message,"test boota")

@bot.message_handler (commands=['help'])
def hello(message):
    bot.send_message(message.chat.id, menu)

#marks last 7 days
@bot.message_handler (regexp='src([mr])$')
def hello(message):
    #id = message.text.split('.')
    message.text = message.text.lower()
    pattern = 'src([mr])$'
    id =  re.search(pattern,message.text)
    print(id.group(1))
    oceny = analyzer.AnaLyze(ids_dict[id.group(1)])
    bot.send_message(message.chat.id, oceny.average_total, parse_mode='HTML')

#average for subjects
@bot.message_handler (regexp='sr([mr])$')
def hello(message):
    #id = message.text.split('.')
    message.text = message.text.lower()
    pattern = 'sr([mr])$'
    id =  re.search(pattern,message.text)
    print(id.group(1))
    oceny = analyzer.AnaLyze(ids_dict[id.group(1)])
    bot.send_message(message.chat.id, oceny.average_all, parse_mode='HTML')

#marks last 7 days
@bot.message_handler (regexp='o([mr])$')
def hello(message):
    #id = message.text.split('.')
    message.text = message.text.lower()
    pattern = 'o([mr])$'
    id =  re.search(pattern,message.text)
    print(id.group(1))
    oceny = analyzer.AnaLyze(ids_dict[id.group(1)])
    bot.send_message(message.chat.id, oceny.grade_by_subject(), parse_mode='HTML')

#marks / day
@bot.message_handler (regexp='o([mr])([0-9]+)$')
def hello(message):
    #id = message.text.split('.')
    message.text = message.text.lower()
    pattern = 'o([mr])([0-9]+)$'
    id =  re.search(pattern,message.text)
    oceny = analyzer.AnaLyze(ids_dict[id.group(1)])
    bot.send_message(message.chat.id, oceny.grade_by_subject(days_param=int(id.group(2))), parse_mode='HTML')

#marks / subject
@bot.message_handler (regexp='o([mr])([a-z]+)$')
def hello(message):
    #id = message.text.split('.')
    message.text = message.text.lower()
    pattern = 'o([mr])([a-z]+)$'
    id =  re.search(pattern,message.text)
    print(id.group(1))
    oceny = analyzer.AnaLyze(ids_dict[id.group(1)])
    bot.send_message(message.chat.id, oceny.grade_by_subject(subject_finder=id.group(2), days_param=10), parse_mode='HTML')

#marks / subject / day
@bot.message_handler (regexp='o([mr])([a-z]+)([0-9]+)$')
def hello(message):
    #id = message.text.split('.')
    message.text = message.text.lower()
    pattern = 'o([mr])([a-z]+)([0-9]+)$'
    id =  re.search(pattern,message.text)
    print(message.chat.id)
    oceny = analyzer.AnaLyze(ids_dict[id.group(1)])
    bot.send_message(message.chat.id, oceny.grade_by_subject(subject_finder=id.group(2), days_param=int(id.group(3))), parse_mode='HTML')

bot.polling()

#bot.send_message('-1001683127782', 'aaa')