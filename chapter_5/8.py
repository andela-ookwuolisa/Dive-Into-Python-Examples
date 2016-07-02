class Foo:
    pi = 3.14159
    common_var = 5

    def __init__(self, var):
        self.common_var = var

print "pi is: " + str(Foo.pi)  # Accessing pi without creating Foo's instance
print "Common var is: " + str(Foo.common_var)

f = Foo(10)

print "f.pi: " + str(f.pi)
# local namespace and class namespace
print "f.common_var: " + str(f.common_var)  # Try to guess the output
print "Foo.common_var: " + str(Foo.common_var)

# Remember search space is local namespace > class namespace
