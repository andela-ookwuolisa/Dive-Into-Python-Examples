def divide(var1, var2):
    try:
        print 'dividing {0} by {1}'.format(var1, var2)
        res = var1 / var2
        print res
    except:
        print 'Cannot divide by {0}'.format(var2)
    else:
        print 'Division is successful'


var1 = 86
divide(var1, 5)
print
divide(var1, 'PT')
print
