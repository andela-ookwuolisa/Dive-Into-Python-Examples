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

# ****************************  ********** SOLUTION *********  **************************************** #

# this prints the methods of new_class
print dir(new_class)

# this prints the type of pupil
print type(pupil)

# this checks if method new_class.register is callable
print callable(new_class.register)

# this prints all scores less that 50
new_list = [score for score in pupil_score if score < 50]
print new_list

# this converts new_list to a string
new_list = str(new_list)
print type(new_list)

# this test if the lenght of pupil and pupil_score is same
if len(pupil) == len(pupil_score):
    print "All students took the test"

