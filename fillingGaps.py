#!/usr/bin/python3

import os, re, shutil

dir = '/home/iliya/repository/AutomateTheBoringStuffWithPython/fillingGaps'

seq = re.compile(r'^(spam)(\d+)(.txt)')

lst = []
for file in os.listdir(dir):
    num = seq.search(file).group(2)
    lst.append( (int(num.lstrip('0')), file, len(num)) )

lst = sorted(lst)
for index in range(len(lst)):
    padding = lst[index][2]
    num = str(int(index) + 1)
    padded_num = num.rjust(padding, '0')
    src = os.path.join(dir, lst[index][1])
    dst = os.path.join(dir, seq.sub(r'\g<1>%s\g<3>' % padded_num, lst[index][1]))
    shutil.move(src, dst)
# for i in 001 002 004 005 006 009 ; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt ; done
# for i in 011 012 014 025 026 319 ; do touch ${dir}/spam$i.txt ; echo $i > ${dir}/spam$i.txt ; done
