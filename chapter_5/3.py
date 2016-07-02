class FirstClass:
    """Simple class with method say_hi"""

    def say_hi(self, name="anonymous"):
        # Don't worry about `self`. We will come back to that soon
        print "Hi, " + name

first_object = FirstClass()  # Creating object of FirstClass
first_object.say_hi("Python")  # Calling method of FirstClass

second_object = FirstClass()
second_object.say_hi("Spam")
