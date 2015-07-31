#!/usr/bin/python3

# walks through a folder tree and searches for files with .py file extension. Archive these files in to a ZIP file

import os, sys, shutil
from zipfile import ZipFile


def main(dir):
    dir = '/home/iliya/repository'
    zip_file = os.path.join(dir, 'python_scripts.zip')
    extension = '.py'
    backup(dir, zip_file, extension)
    print('Destination ZIP file: %s' % zip_file)

def backup(dir, zip_file, extension):
    with ZipFile(zip_file, 'w') as zip:
        for dirname, subdirs, basename in os.walk(dir):
            lst = [x for x in basename if x.endswith(extension)]
            if len(lst) > 0:
                for file in lst:
                    zip.write(os.path.join(dirname, file))
        zip.close()

if __name__ == '__main__':
    main(dir)
