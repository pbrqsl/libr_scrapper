from selenium.webdriver.common.by import By

class MessageLocators:
    #log in page
    MESSAGE_AUTOR_LOCATOR = By.XPATH, 'td[@class="micro center"]//following-sibling::td[2]/a'
    MESSAGE_TITLE_LOCATOR = By.XPATH, 'td[ @class ="micro center"] // following-sibling::td[3]/a'
    MESSAGE_DATE_LOCATOR = By.XPATH, 'td[@class ="micro center"] // following-sibling::td[4]'
    MESSAGE_ITEM_LOCATOR = By.XPATH, '//tbody/tr[starts-with(@class,"line")]'

