s = '100 NORTH MAIN ROAD'
res = s.replace('ROAD', 'RD.') 
print('%s ===> %s' % (s, res))
s = '100 NORTH BROAD ROAD'
res = s.replace('ROAD', 'RD.') 
print('%s ===> %s' % (s, res))
res = s[:-4] + s[-4:].replace('ROAD', 'RD.')
print('%s ===> %s' % (s, res))