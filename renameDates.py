#!/usr/bin/python3

# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import re, os, shutil

# Create a regex that matches files with the American date format .
datePattern = re.compile(r"""
    ^(.*?)                      # all text before the date
    (\b|_)                      # boundary
    ((?:0?[1-9]|1[0-2])-)       # one or two digits for the month 1-12
    ((?:0?[1-9]|[12]\d|3[01])-) # one or two digits for the day 1-31
    ((?:19[7-9]|20[01])\d)      # four digits for the year 1970-2019
    (\b|_)                      # boundary
    (.*?)$                      # all text before the date
    """, re.VERBOSE)

current_dir = os.getcwd()
# Loop over the files in the current directory recursively.
for pathname, subdir, basename in os.walk(current_dir):
    # create list of tuples containing source and destination absolute pathes
    pair = [(os.path.join(pathname, x), os.path.join(pathname, datePattern.sub(r'\1\2\4\3\5\6\7', x))) for x in basename if datePattern.search(x)]
    # Rename the files
    if len(pair) == 0:
        continue
    print(pair)
    for source, destination in pair:
        shutil.move(source, destination)

# create files for testing
# for i in $(seq 1 11) ; do touch test$i ; done
# for i in $(seq 1 12) ; do touch $i-30-2011 ; done
# for i in $(seq 1 12) ; do touch $i-30-1986.gz ; done
# for i in $(seq 1 12) ; do touch myne_$i-30-2011.txt ; done
# for i in $(seq 1 12) ; do touch iliya-$i-25-2011.tar.txt ; done
