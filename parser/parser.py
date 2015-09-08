import bs4 from BeautifulSoup

class TimetableParser:

    def __init__(self, timetable):
        self.timetable = timetable
        self.dailyClasses = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
