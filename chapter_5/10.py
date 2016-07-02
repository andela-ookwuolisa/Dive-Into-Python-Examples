class Pet:

    def __init__(self, name, color):
        self.name = name
        self.color = color

# Cat class inherited from Pet class
class Cat(Pet):

    def purr(self):
        print "Purr.."

# Dog class inherited from Pet class
class Dog(Pet):

    def bark(self):
        print "Woo!"

# Notice we don't have __init__ method in Dog class but __init__ method
# is present in Dog class through Pet class
fido = Dog("Fido", "Brown")
print fido.color
fido.bark()

lucy = Cat("Lucy", "Black")
print lucy.color
lucy.purr()

# You cannot call a method from one derived class to other derived class
# If they both don't share any similarity For ex:
# fido.purr() will through exception
# same with lucy.bark()
