import re

p = re.compile('^.rodo$')
m = p.match('frodo')
if m:
    print('match found: ', m.group())  # match found python
else:
    print('no match')
