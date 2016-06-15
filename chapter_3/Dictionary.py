__author__ = 'djff'

# This file will go through explaining dictionary using code example

# Dictionaries are key:value mapping of elements placed in curly brackets

# Dictionaries can be defined using the {} or the dict() class.

# Defining a dictionary called class_teacher using {}
class_teacher = {'form1': 'Epote', 'form2': 'Kingsley', 'form3': 'Ashley', 'form4': 'Stephen'}

# This prints out the dictionary on screen.
print "\n***** Dictionary created using {} *****"
print class_teacher

# Defining a dictionary called class_teacher using dict() class.
class_teacher = dict(form1='Epote', form2='Kingsley', form3='Ashley', form4='Stephen')

# this prints out the dictionary on screen.
print "\n***** Dictionary created using dict() class *****"
print class_teacher

# To get the teacher of form2 we access dictionary using class_teacher['form2']
# if you access using the value of key, a KeyError will be thrown

# this prints out the teacher of form2.
print '\n***** Retrieving teacher of form2: *****'
print class_teacher['form2']

# If you want to change the teacher of form3 to Greezeman you use class_teacher['form3'] = 'Greezeman'

# This changes teacher of form3 to Greezeman
class_teacher['form3'] = 'Greezeman'

# print this is the new dictionary
print "\n***** Modifying teacher of form3 to Greezeman*****"
print class_teacher

# To add a new key:value to the dictionary we use class_teacher['key']='value'

# this adds form5:'Cloe' to dictionary
class_teacher['form5'] = 'Cloe'

# this is new dictionary content
print "\n***** adding form5:Cloe to dictionary *****"
print class_teacher

# to delete an entry from dictionary, we use the key work 'del'

# this deletes form2 from the dictionary.
del class_teacher['form2']

# Content of dictionary after deleting
print "\n***** deleting form2 from the dictionary *****"
print class_teacher

# To iterate over a dictionary, we use the for loop

# This iterates over a dictionary and print the key:value pair using .items() method
print "\n**** Iterating in dictionary to get key:value pairs *****"
for key, value in class_teacher.items():
    print "%s:%s" % (key, value)

# This iterates over a dictionary and prints only the keys using .keys() method
print "\n**** Iterating in dictionary to get all keys *****"
for key in class_teacher.keys():
    print key

# This iterates over a dictionary and prints only the Values using .value() method
print "\n**** Iterating in dictionary to get all values *****"
for value in class_teacher.values():
    print value











