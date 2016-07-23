import re

strings_to_match = [
    '800-555-1212',
    '800 555 1212',
    '800.555.1212',
    '(800) 555-1212',
    '1-800-555-1212',
    '800-555-1212-1234',
    '800-555-1212x1234',
    '800-555-1212 ext. 1234',
    'work 1-(800) 555.1212 #1234',
    '80055512121234'
]

verbose_pattern = r'''
                            # don't match beginning of string, number can start anywhere
    (?P<area_code>\d{3})    # area code is 3 digits (e.g. '800')
    \D*                     # optional separator is any number of non-digits
    (?P<trunk>\d{3})        # trunk is 3 digits (e.g. '555')
    \D*                     # optional separator
    (?P<number>\d{4})       # rest of number is 4 digits (e.g. '1212')
    \D*                     # optional separator
    (?P<extension>\d*)      # extension is optional and can be any number of digits
    $                       # end of string
    '''
compiled_pattern = re.compile(verbose_pattern, re.VERBOSE) 

for s in strings_to_match:
    print(s)
    res = compiled_pattern.search(s)
    print(res.groupdict() if res else 'No groups were found.')
    print