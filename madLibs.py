#!/usr/bin/python3

import shelve, sys

with shelve.open('madLibs_file') as my_file:
    for word in ['ADJECTIVE', 'NOUN', 'VERB']:
        my_file[word] = input('Enter an %s: ' % word)

    with open('madLibs.txt', 'r') as file:
        for word in file.read().split(' |.'):
            if word in list(my_file.keys()):
                print(my_file[word])
            else:
                print(word)
    file.close()
my_file.close()
#sys.exit()
