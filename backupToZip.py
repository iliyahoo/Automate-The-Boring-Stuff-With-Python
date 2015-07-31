#!/usr/bin/python3

# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, sys
from zipfile import ZipFile

dir = '/home/iliya/repository/AutomateTheBoringStuffWithPython'

def main(dir):
    folder = os.path.abspath(dir)
    backupToZip(folder)

def backupToZip(folder):
    number = 1
    while True:
        zipFileName = os.path.join(dir, os.path.basename(dir) + '_' + str(number) + '.zip')
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Creating the ZIP file
    print('Creating %s... ' % zipFileName)
    with ZipFile(zipFileName, 'w') as backupZip:
        for dirname, subdir, basename in os.walk(dir):
            print('Adding files in %s... ' % dirname)
            # Add the current folder to the ZIP file.
            backupZip.write(dirname)
            # Add all files in that folder to the ZIP file.
            for file in basename:
                if file.startswith(os.path.basename(dir) + '_') and file.endswith('.zip'):
                    continue # don't backup the backup ZIP file
                backupZip.write(os.path.join(dirname, file))
        print('Done.')
        backupZip.close()

if __name__ == '__main__':
    main(dir)
