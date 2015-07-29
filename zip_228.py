#!/usr/bin/python3

from zipfile import ZipFile
import os, sys

zip = 'example.zip'
dir = zip.split('.')[0]
os.chdir('automate_online-materials')

exampleZip = ZipFile(zip)
#print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('spam.txt')
#print(spamInfo.file_size)
#print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / float(spamInfo.compress_size), 2)))

exampleZip.extractall(dir)
exampleZip.extract('spam.txt', dir + '_r2')
exampleZip.close()
sys.exit()
