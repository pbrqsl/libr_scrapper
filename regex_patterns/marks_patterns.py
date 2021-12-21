class MarksPatterns:
    MARK_COMMENT = 'Komentarz: (.*)'
    MARK_CATEGORY = 'Kategoria: (.*)<br>Data'
    MARK_DATE = 'Data: (\d{4}-\d{2}-\d{2})'
    MARK_AVERAGE = 'Licz do .redniej: (\w+)'
    MARK_FACTOR = 'Waga: (\d+)'
    MARK_CORRECTION = 'Poprawa oceny: (.*)$'