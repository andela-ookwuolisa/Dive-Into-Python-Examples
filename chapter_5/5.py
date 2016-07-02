class Spam:

    def __repr__(self):
        return "This is a Spam instance"

s = Spam()

print str(s)  # Calling str which will call repr
print s.__repr__()  # Explicitly calling repr
print s  # Implicity Python interpreter will call repr for us
