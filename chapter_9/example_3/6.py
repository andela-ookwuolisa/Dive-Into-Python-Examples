s = 'La Pe\xf1a'

# Below line will print a wierd character instead of what we are expecting
print type(s)
print s

s = u'La Pe\xf1a'
print type(s)
print s
