import re

p = re.compile('[a-z]+')
m = p.match('python')
if m:
    print('match found: ', m.group())  # match found python
else:
    print('no match')
