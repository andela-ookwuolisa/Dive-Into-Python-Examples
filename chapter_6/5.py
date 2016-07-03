f = open('foo2.txt', 'w')
# New file foo.txt will be created and if already exists then all the previous
# data from foo.txt will be lost.

for i in xrange(5):
    s = raw_input("Enter {0}st line into file: ".format(i + 1))
    # Write into file
    f.write(s)

# Attempt to read from file will produce error
# f.read()

# Finally close the file.
f.close()
