import logging

logger = logging.getLogger('libscrap.markslogic')

class MarksLogic():


    @classmethod
    def check_for_new_marks(cls,new_marks, old_marks):

        logger.info('checking for new marks')
        cls.old_marks = old_marks
        cls.new_marks = new_marks
        cls.new_marks_dict = {}

        for key in cls.new_marks.keys():
            for new_mark in cls.new_marks[key]:
                if new_mark not in cls.old_marks[key]:
                    if key not in cls.new_marks_dict:
                        cls.new_marks_dict[key] = [new_mark]
                    else:
                        cls.new_marks_dict[key].append(new_mark)

        return cls.new_marks_dict

    @classmethod
    def check_for_removed_marks(cls,new_marks, old_marks):
        cls.old_marks = old_marks
        cls.new_marks = new_marks
        cls.removed_marks_dict = {}

        for key in cls.old_marks.keys():
            for old_mark in cls.old_marks[key]:
                if old_mark not in cls.new_marks[key]:
                    if key not in cls.removed_marks_dict:
                        cls.removed_marks_dict[key] = [old_mark]
                    else:
                        cls.removed_marks_dict[key].append(old_mark)

        return cls.removed_marks_dict


    @classmethod
    def format_mark(cls, mark):
        #format:
        #{'mark_value': '5', 'factor': '5', 'average': 'tak', 'category': 'sprawdzian', 'mark_date': '2021-10-06',
        #'comment': 'skóra- powłoka organizmu', 'correction': '0'}
        return f'<b>{mark["mark_value"]}</b>,[x{mark["factor"]}] ,Data: {mark["mark_date"]}, komentarz: {mark["comment"]}, katergoria: {mark["category"]}\n'


    @classmethod
    def generate_marks_change_message(cls, new_marks, old_marks):
        added_marks = MarksLogic.check_for_new_marks(new_marks, old_marks)
        removed_marks = MarksLogic.check_for_removed_marks(new_marks, old_marks)

        message = ''
        if added_marks:
            logger.info('Found new marks')
            message += f'Dodano oceny: \n'

            for marks in added_marks:
                message = message + f'{marks}: '
                print(marks)
                for mark in added_marks[marks]:
                    print(mark)
                    message = message + MarksLogic.format_mark(mark)
            message = message + '\n'
        else:
            logger.info('No new marks found')


        if removed_marks:
            logger.info('Found removed marks')
            message += f'Usunięto oceny: \n'

            for marks in removed_marks:
                message = message + f'{marks}: '
                for mark in removed_marks[marks]:
                    message = message + MarksLogic.format_mark(mark)

        else:
            logger.info('No removed marks found')
        return message
