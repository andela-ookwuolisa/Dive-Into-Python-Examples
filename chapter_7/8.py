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


pattern = r'^(\d{3})\D+(\d{3})\D+(\d{4})\D*(\d*)$'
compiled_pattern = re.compile(pattern)

for s in strings_to_match:
    print(s)
    res = compiled_pattern.search(s)
    print(res.groups() if res else 'No groups were found.')
    print