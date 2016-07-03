# Output of this program may differ from os to os. See output.txt for output
# on my os

import os
print 'changing directory to Desktop\n'
os.chdir('/home/deepanshu/Desktop')

print 'Getting current working directory: ',
print os.getcwd()

print '\nJoining path: ' + os.path.join('/home/deepanshu/Desktop', 'foo.txt'),

print '\nExample of expanduser: ',
print os.path.expanduser('~')

print '\nPrinting 5 files from my Desktop: '
lst = os.listdir(os.path.expanduser('~') + '/Desktop')
for i in xrange(5):
    print lst[i],
print

print 'Creating Directory Daniel'
# This will create a Daniel directory in current working directory
os.mkdir('Daniel')

print 'Now changing to Daniel directory'
os.chdir('Daniel')

print 'Now current working directory is: ',
print os.getcwd()
