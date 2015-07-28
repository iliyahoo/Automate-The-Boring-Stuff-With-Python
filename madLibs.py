#!/usr/bin/python3

import shelve, sys

with shelve.open('madLibs') as madLibs:
    for word in ['ADJECTIVE', 'NOUN', 'VERB']:
        madLibs[word] = input('Enter an %s: ' % ADJECTIV)
        print(list(madLibs.items()))
madLibs.close()

with open('madLibs.txt', 'r') as file:
    for line in file.readlines():
        print(line)
file.close()
