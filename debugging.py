#!/usr/bin/python3

import sys, traceback

assert_key = 'test'

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try:
    assert_key = 'Faled.'
    assert assert_key == 'test', 'assert_key should be "test" always'
    spam()
except:
    with open('errorInfo.log', 'a') as errorFile:
        errorFile.write(traceback.format_exc())
        errorFile.write('\n\n')
        errorFile.close()
    print('The traceback info was written to errorInfo.log')
sys.exit()

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol "%s" must be a single character string.' % symbol)
    if width <= 2:
        raise Exception('Width "%s" must be greater than 2.' % width)
    if height <= 2:
        raise Exception('Height "%s" must be greater than 2.' % height)
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3 ), ('ZZ', 3, 3 )):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: %s' % err)
