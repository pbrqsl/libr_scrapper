import random
import time
import re
from locators.marks_page_locators import MarksLocators
from selenium.webdriver.common.by import By
from regex_patterns.marks_patterns import MarksPatterns
import logging


# logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#                     datefmt='%d-%m-%Y %H:%M:%S',
#                     level=logging.INFO,
#                     filename='logs.txt')

logger = logging.getLogger('libscrap.marks_parser')

class MarksPage:
    def __init__(self, marks_page):
        self.page = marks_page
        logger.info('Initializing marks page')

    @property
    def all_marks(self):
        logger.debug('Starting all marks function')
        subjects = self.subjects_names
        #subjects = ["Matematyka", "Plastyka"]
        subjects.remove('Zachowanie')
        marks = {}
        for subject in subjects:
            logger.debug(f'Getting marks for {subject} and adding to dictionary')
            marks[subject] = self.get_marks_for_subject(subject)
        return (marks)


    @property
    def subjects_ids(self):
        ids = self.page.find_elements(*MarksLocators.SUBJECTS_ID_LOCATOR)

        id_list = [id.get_attribute('id') for id in ids if id.get_attribute('id') != '']
        return list(id_list)

    @property
    def subjects_names(self):
        logger.debug('generating list of subject names webelements [subject_names func]')
        names = self.page.find_elements(*MarksLocators.SUBJECTS_NAME_LOCATOR)
        #print(len(names))
        logger.debug('extracting text from subject names webelements [subject_names func]')
        names_list = [name.text for name in names if name.text != ' ']
        return names_list


    def get_marks_for_subject(self, subject_name):
        logger.debug('[get_marks_for_subject] getting marks for subject')
        marks_subject = self.page.find_elements(By.XPATH, f'//td[text()="{subject_name}"]//following-sibling::td')
        marks_list = []
        for mark_subject_element in marks_subject:
            marks_list.append(self.extract_marks(mark_subject_element))
        # following columns contain marks: 0,2, 3, 5, 7 approprietly for 1sem, 1sem_final, 2sem, 2sem_final, year_final
        marks_list_temp = [marks_list[0], marks_list[2], marks_list[3], marks_list[5], marks_list[7]]
        semesters = ['1', '1', '2', '2', '2']
        for marks, semester in zip(marks_list_temp, semesters):
            if marks:
                for mark in marks:
                    mark['semester'] = semester
        marks_list = []
        for list in marks_list_temp:
            marks_list.extend(list)

        return marks_list

    def extract_marks(self, many_marks):
        logger.debug('[extract_marks] start')
        marks_list = many_marks.find_elements(*MarksLocators.EXTRACT_MARKS_LOCATOR)
        marks = []
        for mark in marks_list:
            logger.debug('[extract_marks] extracting mark...')
            marks.append(self.mark_details(mark))
        return marks



    def mark_details(self,mark):
        logger.debug('[mark_details] start')
        logger.debug(f'[mark_details] extracting summary from mark: {mark.get_attribute("outerHTML")}')
        summary = mark.find_element(*MarksLocators.SUMMARY_LOCATOR)
        logger.debug('[mark_details] getting text with mark attributes')
        summary_text = summary.get_attribute('title')
        logger.debug(f'[mark_details] starting regex extract from {summary_text}')

        # pattern_category = 'Kategoria: (.*)<br>Data'
        # pattern_date = 'Data: (\d{4}-\d{2}-\d{2})'
        # pattern_average = 'Licz do .redniej: (\w+)'
        # pattern_factor = 'Waga: (\d+)'
        #comment = re.search(pattern_comment, summary_text)
        logger.debug('[mark_details] extracting comment')
        comment = re.search(MarksPatterns.MARK_COMMENT, summary_text)
        logger.debug('[mark_details] extracting category')
        category_extract = re.search(MarksPatterns.MARK_CATEGORY, summary_text)
        category = category_extract.group(1) if category_extract != None else '0'
        logger.debug('[mark_details] extracting date')
        mark_date_extract = re.search(MarksPatterns.MARK_DATE, summary_text)
        mark_date = mark_date_extract.group(1) if mark_date_extract != None else '0'
        logger.debug('[mark_details] extracting average')
        average_extract = re.search(MarksPatterns.MARK_AVERAGE, summary_text)
        average = average_extract.group(1) if average_extract != None else '0'
        logger.debug('[mark_details] extracting factor')
        factor_extract = re.search(MarksPatterns.MARK_FACTOR, summary_text)
        factor = factor_extract.group(1) if factor_extract != None else '0'
        logger.debug('[mark_details] extracting correction')
        correction_extract = re.search(MarksPatterns.MARK_CORRECTION, summary_text)
        correction = correction_extract.group(1) if correction_extract != None else '0'
        logger.debug('[mark_details] extracting comment')
        comment = comment.group(1) if comment != None else '0'
        mark_value = summary.text
        logger.debug('[mark_details] building mark dict')
        mark_dict = {
            'mark_value': mark_value,
            'factor': factor,
            'average': average,
            'category': category,
            'mark_date': mark_date,
            'comment': comment,
            'correction': correction
        }
        logger.debug('[mark_details] returning mark dict')
        return mark_dict

    '''
    marks = [(mark, wage, date, notes),] 
        
    '''