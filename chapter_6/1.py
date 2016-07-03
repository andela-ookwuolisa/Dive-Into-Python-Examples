# Simple python program to show use of try-except block

def divide_1(var1, var2):
    # Generic except block to catch all types of exceptions
    try:
        print var1 / var2
    except:
        print 'Cannot divide by {0}'.format(var2)


def divide_2(var1, var2):
    # Handling exception with exception name
    # This function will only handle exception when var2 is 0
    # and throw exception if var2 cannot divide var1 for example if var2
    # is string
    try:
        print var1 / var2
    except ZeroDivisionError:
        print 'Cannot divide by 0'

def divide_3(var1, var2):
    # Multiple except blocks are allowed
    try:
        print var1 / var2
    except ZeroDivisionError:
        print 'Cannot divide by 0'
    except TypeError:
        print 'Cannot divide by {0}'.format(var2)
    # You can write above two except like this too
    # except ZeroDivisionError, TypeError:
    #     print 'Cannot perform operation'
    # You can write a generic except here too
    except:
        print 'Unknown error occurred'


var1 = 5
# divide_1 will handle any type of exception
print 'Trying divide_1'
divide_1(var1, 5)
divide_1(var1, 0)
divide_1(var1, 'FooBarBaz')
print '\n' * 3

# divide_2 will handle only Zero Divison Error
print 'Trying divide_2'
divide_2(var1, 0)
# divide_2(var1, 'BazBarFoo')  # Will throw exception
print '\n' * 3

# divide_3 will try to handle Zero Division Error and Type error and
# if exception is neither ZeroDivision nor TypeError than generic except
# will catch it
print 'Trying divide_3'
divide_3(var1, 0)
divide_3(var1, 'EggSpam')
divide_3(var1, 'Try to create a new exception with this argument')
