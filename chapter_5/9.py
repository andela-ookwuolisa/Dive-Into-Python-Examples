class Nine:

    def __init__(self):
        print "instance is created"
        self._instance_count = 0
        self.__strongly_private = 0

    # This is how you should access private attributes
    def print_instance_count(self):
        print 'instance count is: ' + str(self._instance_count)

    # This is how you should access private attributes
    def print_strongly_private(self):
        print 'value of strongly private is ' + str(self.__strongly_private)

    def increment(self):
        self._instance_count += 1
        self.__strongly_private += 1


i1 = Nine()
i1.print_instance_count()
i1.print_strongly_private()
print
print 'After incrementing values: \n'
i1.increment()
i1.print_instance_count()
i1.print_strongly_private()

print
print 'After accessing values and changing them \n'

# You should never do this. Just to show that nothing is truly private
i1._instance_count += 1
i1._Nine__strongly_private += 7
print 'instance count: ' + str(i1._instance_count)
print 'strongly private: ' + str(i1._Nine__strongly_private)
# This line will cause error saying no attribute find
print i1.__strongly_private
