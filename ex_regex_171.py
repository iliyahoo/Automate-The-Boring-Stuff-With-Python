#!/usr/bin/python3

import re

text = 'Wfdgff4fde'

mo = re.compile(r'''
    \b
    (?=.*\d)
    (?=.*[a-z])
    (?=.*[A-Z]).{8,}
    \b
''', re.VERBOSE)

print(mo.findall(text))
