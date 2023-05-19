# student.py

class Student:

    def __init__(self):
        self.hours = 0.0
        self.qpoints = 0.0

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        self.hours = self.hours + credits
        self.qpoints = self.qpoints + gradePoint * credits

