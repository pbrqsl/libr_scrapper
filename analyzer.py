from utils.filer import FileOperations
import time
import datetime
from datetime import datetime, timedelta





plus_factor = 0.5
minus_factor = 0.25


'6186174'
class AnaLyze:
    def __init__(self, id):
        self.id = id
        self.marks = FileOperations.load_marks_file(self.id)
        self.subjects = self.marks.keys()


    def average_grade(self, subject):
        total_value = 0
        total_weigh_mark = 0
        mark_count = 0
        mark_count_w = 0
        total_factor = 0
        for mark in self.marks[subject]:
            calc_mark = self.calc_grade(mark['mark_value'])
            if isinstance(calc_mark, float):
                total_value += calc_mark
                total_weigh_mark += (calc_mark * int(mark['factor']))
                if calc_mark != 0:
                    mark_count += 1
                if calc_mark * int(mark['factor']) != 0:
                    total_factor += int(mark['factor'])
            else:
                #print(mark["mark_value"])
                pass
        if mark_count!= 0:
            average = total_value / mark_count

        else:
            average = 0

        if total_factor != 0:
            weighted_average = total_weigh_mark / total_factor
        else:
            weighted_average = average
        return average, weighted_average


    def calc_grade(self, grade):
        try:
            grade_value = float(grade[0])
            if '+' in grade:
                grade_value = grade_value + plus_factor
            elif '-' in grade:
                grade_value = grade_value - minus_factor
            return grade_value
        except:
            return grade

    @property
    def average_all(self):
        grades_list = ''
        for subject in self.subjects:
            average = "{:.1f}".format(self.average_grade(subject)[0])
            weighted = "{:.1f}".format(self.average_grade(subject)[1])
            grades_list = grades_list + f'{subject}: {average} | {weighted}\n'
        return grades_list

    @property
    def average_total(self):
        total_average = 0
        total_weighted = 0
        count = 0
        count_weight = 0
        for subject in self.marks.keys():
            total_average += self.average_grade(subject)[0]
            total_weighted += self.average_grade(subject)[1]
            if self.average_grade(subject)[0] != 0:
                count += 1
            if self.average_grade(subject)[1] != 0:
                count_weight += 1
        print(total_average)
        print(count)
        total_average = "{:.2f}".format(total_average / count)
        total_weighted = "{:.2f}".format(total_weighted / count)
        result = f'Średnia arytmetyczna: {total_average}\nŚrednia ważona: {total_weighted}'
        return result

    def grade_by_subject(self, subject_finder: str = '', days_param: int = 7):
        result_dict = {}
        today = datetime.now()
        date_from = today - timedelta(days = days_param)

        for subject in self.subjects:
            if subject_finder.lower() in subject.lower():
                for mark in self.marks[subject]:
                    mark_date = datetime.strptime(mark['mark_date'], '%Y-%m-%d')
                    if mark_date > date_from:
                        if subject in result_dict:
                            result_dict[subject].append(mark)
                        else:
                            result_dict[subject] = [(mark)]
        return f'Oceny z osatnich {days_param} dni: \n{self.read_school_diary(result_dict)}'


    def read_school_diary(self, diary):
        diary_result = ''
        for subject in diary:
            result = f'{subject}: '
            for mark in diary[subject]:
                result += f"<b>{mark['mark_value']}</b><i>[x{mark['factor']}]({mark['mark_date'][-5:].replace('-','.')})</i>,"
            result = result[:-1] + '\n\n'
            diary_result += result
        return diary_result


if __name__ == '__main__':
    grades = AnaLyze('4394568')
    print(grades.average_all)
    print(grades.average_total)
    print(grades.grade_by_subject('yka'))

'4394568'
'6186174'

