import re

s = '100 BROAD ROAD'

regex = '\\bROAD$'
res = re.sub(regex, 'RD.', s)  
print('%s ===> %s # using regex %s' % (s, res, regex))

regex = r'\bROAD$'
res = re.sub(regex, 'RD.', s)  
print('%s ===> %s # using regex %s' % (s, res, regex))

s = '100 BROAD ROAD APT. 3'
regex = r'\bROAD$'
res = re.sub(regex, 'RD.', s)  
print('%s ===> %s # using regex %s' % (s, res, regex))

regex = r'\bROAD\b'
re.sub(regex, 'RD.', s) 
print('%s ===> %s # using regex %s' % (s, res, regex))
