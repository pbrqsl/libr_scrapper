from selenium.webdriver.common.by import By

class MarksLocators:
    #log in page
    #ZALOGUJ_MENU_LOCATOR = By.CSS_SELECTOR, 'a.btn.btn-third.btn-synergia-top'
    SUBJECTS_ID_LOCATOR = By.CSS_SELECTOR, 'tr[class^="line"] img'
    #SUBJECTS_NAME_LOCATOR = By.XPATH, '//tr[starts-with(@class,"line") and not(@id="przedmioty_zachowanie")]/td[2][not(@id) and not(@class) and not(@name) and text()]'
    SUBJECTS_NAME_LOCATOR = By.XPATH, '//td[@class = "center micro screen-only"]//following-sibling::td[1]'
    #MARKS_SECTION_LOCATOR = By.XPATH, '//td[text()="Biologia"]//following-sibling::td'

    #ZALOGUJ_BUTTON_LOCATOR = By.PARTIAL_LINK_TEXT, 'Zaloguj'
    # subject_name = ''
    # MARKS_FOR_SUBJECT= By.XPATH, f'//td[text()="{subject_name}"]//following-sibling::td'
    EXTRACT_MARKS_LOCATOR = By.XPATH, 'span[starts-with(@id,"Ocena")]|span/span[starts-with(@id,"Ocena")]'
    SUMMARY_LOCATOR = By.CSS_SELECTOR, 'a'