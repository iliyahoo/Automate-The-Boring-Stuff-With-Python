#!/usr/bin/python3

import zipfile, os, sys

newZip = zipfile.ZipFile('new.zip')
print(newZip.namelist())
sys.exit()

newZip = zipfile.ZipFile('new.zip', 'a')
newZip.write('myPets.py', compress_type=zipfile. ZIP_DEFLATED)
newZip.close()
