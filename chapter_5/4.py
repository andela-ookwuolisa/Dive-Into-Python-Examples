class Person:

    """This class define a person in real life having name and age"""

    def __init__(self, name, age=0):
        self.name = name  # As soon as person is created it should have a name
        self.age = age  # and age which is default to 0 (New born baby <3)

    def print_name(self):
        print "My name is: " + self.name

    def print_age(self):
        # To concate age with string we need to convert age into string
        print "I am " + str(self.age) + "years old"

adult = Person("Jeff", 23)  # pass arguments for __init__
new_born_baby = Person("Alice")

adult.print_name()
adult.print_age()
new_born_baby.print_name()
