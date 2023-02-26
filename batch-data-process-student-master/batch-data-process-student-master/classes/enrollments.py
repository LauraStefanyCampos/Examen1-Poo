from classes.students import students
from classes.courses import courses

class enrollement():
    def __init__(self,enrollementId,student,course,semester,year):
        self.enrollementId = enrollementId
        self.student = student
        self.course = course
        self.semester = semester
        self.year = year