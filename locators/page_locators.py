from selenium.webdriver.common.by import By

class PageLocators:
    #log in page
    ZALOGUJ_MENU_LOCATOR = By.CSS_SELECTOR, 'a.btn.btn-third.btn-synergia-top'
    ZALOGUJ_BUTTON_LOCATOR = By.PARTIAL_LINK_TEXT, 'Zaloguj'
    LOGIN_NAME_LOCATOR = By.CSS_SELECTOR, 'div#loginRow input#Login'

    #logged in page
    MARKS_LINK_LOCATOR = By.CSS_SELECTOR, 'div#graphic-menu a#icon-oceny'
    MARKS_SUBJECTS_MINI_LOCATOR = By.CSS_SELECTOR, 'tr[class^=""] td.center.micro img'
    MESSAGES_LINK_LOCATOR = By.CSS_SELECTOR, 'div#graphic-menu a#icon-wiadomosci'
    MESSAGES_SECTION_LOCATOR = By.XPATH, '//table[@class = "decorated stretch"]'

    MARKS_SECTION_LOCATOR = By.CSS_SELECTOR, 'div.container'