__author__ = 'djff'

class SchoolClass:
    def __init__(self):
        self.pupil = []
        self.marks = []

    def register(self, stud, mark):
        self.pupil.append(stud)
        if mark:
            self.marks.append(mark)

    def getPupil(self):
        return self.pupil

    def getMarks(self):
        return self.marks

# Creating object of class SchoolClass

new_class = SchoolClass()

# Adding a students and marks

new_class.register('kevin', 30)
new_class.register('stephen', 70)
new_class.register("Caragen", 80)
new_class.register("stephanie", 90)
new_class.register("simpson", 45)
new_class.register("Mary", 40)

pupil = new_class.getPupil()
pupil_score = new_class.getMarks()



# ***************************** PLACE YOUR SOLUTION HERE **************************************** #


