import re

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$' 
print('Pattern is %s.' % pattern)

s = 'MCM'
res = re.search(pattern, s)         # matches one M from the first part, and then CM         
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MD'
res = re.search(pattern, s)         # matches one M from the first part, and then the optional D          
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MMMCCC'
res = re.search(pattern, s)         # matches 3 Ms from the first part, and then 3 Cs               
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MCMC'
res = re.search(pattern, s)         # does not match        
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = ''
res = re.search(pattern, s)         # matches because all Ms are optional and the last exclusive pattern is also optional             
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))
