# Before running this example make sure you have a file name foo.txt in
# currect directory where this program file is saved.

try:
    f = open("foo.txt", 'r')
except IOError:
    print 'File "foo.txt" does not exists please create "foo.txt"'

print 'file mode is: {0}'.format(f.mode)
print 'file name is: {0}'.format(f.name)
print 'file currect position is: {0}'.format(f.tell())
f.seek(-128, 2)
# Now you know above will move left side from the end of the file 128 bytes.
# Remember f.tell() will always give you the file position with respect to the
# start of file.
print 'file position after seek is called is: {0}'.format(f.tell())
f.seek(0)
print 'after seek(0) file position is: {0}'.format(f.tell())
# Move to first position of file
print f.read(14)  # read 12 bytes from file
print 'Now file position is {0}'.format(f.tell())

print 'Now trying to read whole file from the currect position'
print f.read()

# Remeber since we have read entire file. More try to read from file will
# not read any data from it.
print 'Now trying to read from file. Should not read anything from file'
print f.read(10)
f.seek(0)

# Reading line wise line with for loop
print 'We can read file line wise line also for example'
for line in f.readlines():
    print line

# Now you should always close file after using it.
print 'Is file closed? {0}'.format(f.closed)
f.close()
print 'After closing file. Is file really closed? {0}'.format(f.closed)
