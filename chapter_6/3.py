def foo(s="AJOOP"):
    try:
        print 'Trying to import random module'
        x = __import__(s)  # __import__(str) takes a string and returns refrence
        print (x)          # of module
        print 'Import successfully, {0} is importad'.format(s)
    except:
        print 'Cannot import module ' + s
    finally:
        print 'No matter what happens this line should execute'

foo()
print
foo('AJXXOOP')
print
foo('os')
print
