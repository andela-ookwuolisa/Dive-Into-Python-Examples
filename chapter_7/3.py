import re

pattern = '^M?M?M$'   
print('Pattern is %s.' % pattern)    

s = 'M'
res = re.search(pattern, s)    
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MM'
res = re.search(pattern, s)   
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MMM'
res = re.search(pattern, s)  
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MMMM'
res = re.search(pattern, s) #does not match, so nothing is returned
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))
