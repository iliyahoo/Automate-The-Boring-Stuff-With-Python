#!/usr/bin/python3

import os
from send2trash import send2trash

dir = '/home'
size = 1024 # size in MB

multiplicator = 1000 * 1000.0
size = size * multiplicator

large_files = []
for dirname, subdir, basename in os.walk(dir):
    # Ignore mounted remote storage.
    if dirname.startswith('/home/iliya/dune-mountpoint'):
        continue
    large_files.extend( [ (os.path.join(dirname, x), round(os.path.getsize(os.path.join(dirname, x)) / multiplicator, 6)) for x in basename if os.path.getsize(os.path.join(dirname, x)) > size ] )
for path, size in large_files:
    print(path, size)

#    large_files.extend( [ os.path.join(dirname, x) for x in basename if not os.path.exists(os.path.join(dirname, x)) ] )
#for path in large_files:
#    send2trash(path)

