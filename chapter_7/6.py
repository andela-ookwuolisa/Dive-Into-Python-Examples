import re

pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print('Pattern is %s.' % pattern)

s = 'MDLV'
res = re.search(pattern, s)
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MMDCLXVI'
res = re.search(pattern, s)
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'MMMMDCCCLXXXVIII'
res = re.search(pattern, s)
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))

s = 'I'
res = re.search(pattern, s)
print(('Pattern matched string %s.' % s) if res else ('Pattern did NOT match string %s.' % s))
