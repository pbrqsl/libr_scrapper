import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators.page_locators import PageLocators
from parsers.marks_parser import MarksPage

class PageParser:
    def __init__(self, browser):
        self.browser = browser


    def login(self, username:str, password:str):
        button = self.browser.find_element(*PageLocators.ZALOGUJ_MENU_LOCATOR)
        button.click()
        time.sleep(2)
        button2 = self.browser.find_element(*PageLocators.ZALOGUJ_BUTTON_LOCATOR)
        button2.click()
        time.sleep(5)
        actions = ActionChains(self.browser)
        actions.send_keys(username).perform()
        time.sleep(random.randint(1, 3))
        actions.send_keys(Keys.TAB).perform()
        time.sleep(random.randint(1, 3))
        actions.send_keys(password).perform()
        time.sleep(random.randint(1, 3))
        actions.send_keys(Keys.ENTER).perform()


    def go_to_oceny(self):
        time.sleep(3)
        marks = self.browser.find_element(*PageLocators.MARKS_LINK_LOCATOR)
        marks.click()

    def parse_marks(self):
        marks_section = self.browser.find_element(*PageLocators.MARKS_SECTION_LOCATOR)
        #marks_page = MarksPage(marks_section)
        #print(marks_page.subjects_ids)
        #print(marks_page.subjects_names)
        return marks_section

    def go_to_messages(self):
        time.sleep(3)
        marks = self.browser.find_element(*PageLocators.MESSAGES_LINK_LOCATOR)
        marks.click()

    def parse_messages(self):
        messages_section = self.browser.find_element(*PageLocators.MESSAGES_SECTION_LOCATOR)
        #marks_page = MessagesPage(messages_section)
        #print(marks_page.subjects_ids)
        #print(marks_page.subjects_names)
        return messages_section


