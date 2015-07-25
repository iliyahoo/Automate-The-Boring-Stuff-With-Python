#!/usr/bin/python3

import re

text = ' wer 42 1,234 6,368,745 12,34,567 1234 '

mo = re.compile(r'''
    \s
    (\d{1,3}(?:,\d{3})*)
    \s
''', re.VERBOSE)

print(mo.findall(text))
