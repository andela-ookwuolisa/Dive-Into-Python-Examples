class Bird:

    def __init__(self, name):
        self.name = name

    def is_flyable(self):
        return True

class Sparrow(Bird):

    def chrip(self):
        print 'chirp chrip chrip'

class Ostrich(Bird):

    #  Overriding base class method in child class
    def is_flyable(self):
        return False

    def booming(self):
        print 'boom boom boom'

# Using base class's __init__
ostrich = Ostrich("Aust")
sparrow = Sparrow("spy")

# No is_flyable() in child class so call base class's is_flyable
print sparrow.is_flyable()

# is_flyable() found in child class, call it.
print ostrich.is_flyable()
