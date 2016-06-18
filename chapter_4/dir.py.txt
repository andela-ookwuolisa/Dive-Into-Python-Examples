__author__ = 'djff'

#!/usr/bin/python

# dir.py

import sys

# defining a class Object to view the use of dir
class Test:
   def __init__(self):
      pass
   def examine(self):
      print self
   def message(self):
      print "Hello, World!!!"

# initialising the class Object.
o = Test()

print "dir(o) will print the methods of the object of the class test"
print "you can see all the methods which the class implements"
print dir(o)

print "dir([]) will print all the methods implemented in the list class"
print "as we saw in chapter3, [] represents a list"
print dir([])

print "dir({}) will print all the methods implemented in the dictionary class"
print dir({})

print "dir(1) its same as dir(int) which will print all the methods implemented in the integer class"
print "1 is an interger so dir(1) will return methods of an integer, dir('s') will return methods of a string etc"
print dir(1)

print "dir() will print all methods within the context of this file"
print dir()

print "dir(len) will print all methods implemented in the len() class"
print dir(len)

print "dir(sys) will print all methods within the sys module. take note that an import system is first done"
print "*** from modules which are not inbuilt, to use dir() to find its methods, you must first import it"
print dir(sys)

print "as said above for integers dir('String') its same as dir(str) where str is the inbuilt python string class"
print dir("String")