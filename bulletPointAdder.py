#!/usr/bin/python3

import pyperclip

text = pyperclip.paste().split('\n')

mod_text = ''
for line in text:
    mod_text += '* ' + line + '\n'

pyperclip.copy(mod_text)
