#import telegram_send
import time
import telebot
import utils._sec


# class Message2:
#     @classmethod
#     def send_message(cls, friendly_name, message:list):
#         message[0] = f'[{friendly_name}]\n{message[0]}'
#         telegram_send.send(messages=message, parse_mode="html")
#         time.sleep(2)

class Message:

    @classmethod
    def send_message(cls, friendly_name, message:list):
        #api of the telegram bot
        bot = telebot.TeleBot(utils._sec.bot_test_API)
        #id of the Librus updates group
        group_id = '-1001683127782'
        message[0] = f'[{friendly_name}]\n{message[0]}'
        bot.send_message(group_id, message[0], parse_mode='HTML')
        time.sleep(2)

if __name__ == '__main__':
    #Message.send_message('aaa', ['aa'])
    Message1.send_message('aaa', ['<b>a</b>a'])
