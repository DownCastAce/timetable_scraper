import subprocess
import os

class TimetableScraper:
    UL_TIMETABLE_FILE = "tt2.asp"
    UL_TIMETABLE_WEBSITE = "www.timetable.ul.ie/" + UL_TIMETABLE_FILE
    TMP_FILEPATH = "/tmp/"
 
    def __init__(self, param1):
        self.param1 = param1
        self.html = getTimetable()

    def getTimetable(self):
        subprocess.check_output("wget -P " + TMP_FILEPATH + self.param1 + "/ --post-data \"T1=" + self.param1 + "&B1=Submit\" " + UL_TIMETABLE_WEBSITE, shell=True)
        timetable_html = open(TMP_FILEPATH + self.param1 + "/" + UL_TIMETABLE_FILE).read()
        os.system("rm -rf " + TMP_FILEPATH + self.param1)
        return timetable_html
