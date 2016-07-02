class Egg:

    def __init__(self, x=5):
        self.x = x

    def __cmp__(self, other):
        if self.x < other.x:
            return -1
        elif self.x > other.x:
            return 1
        else:
            return 0

e1 = Egg(4)
e2 = Egg(5)
print e1 == e2
print e1 > e2
print e1 < e2
