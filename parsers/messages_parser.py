import random
import time
import re
from locators.message_locators import MessageLocators
from selenium.webdriver.common.by import By
import logging

# logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#                     datefmt='%d-%m-%Y %H:%M:%S',
#                     level=logging.INFO,
#                     filename='logs.txt')

logger = logging.getLogger('libscrap.messages_parser')


class MessagesPage:
    def __init__(self, marks_page):
        self.page = marks_page
        logger.info('Initializing mesages page')

    @property
    def all_messages(self):
        logger.debug('[extract_messages] start')
        messages_list = self.page.find_elements(*MessageLocators.MESSAGE_ITEM_LOCATOR)
        messages = []
        for message in messages_list:
            logger.debug('[extract_messages] extracting mark...')
            messages.append(self.message_details(message))
        return messages

    def message_details(self, message):
        logger.debug('[message_details] start')
        logger.debug(f'[message_details] extracting summary from message: {message.get_attribute("outerHTML")}')
        author = message.find_element(*MessageLocators.MESSAGE_AUTOR_LOCATOR).text
        title = message.find_element(*MessageLocators.MESSAGE_TITLE_LOCATOR).text
        date = message.find_element(*MessageLocators.MESSAGE_DATE_LOCATOR).text
        logger.debug('[message_details] building messages dict')
        messages_dict = {
            'author': author,
            'title': title,
            'date': date
        }
        logger.debug('[message_details] returning mark dict')
        return messages_dict

    '''
    marks = [(mark, wage, date, notes),] 

    '''