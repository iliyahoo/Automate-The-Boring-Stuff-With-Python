#!/usr/bin/python3

import re

text = 'eeeWfdgff4fde'
char = 'e'

def customStrip(text, char):
    mo = re.compile(r'''
        ^
        (?:%s)*(.*?)(?:%s)*
        $
    ''' % (char, char), re.VERBOSE)
    result = mo.sub(r'\1', text)
    return result

print customStrip(text, char)
