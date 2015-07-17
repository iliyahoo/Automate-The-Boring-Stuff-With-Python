#!/usr/bin/python

import sys
from string import maketrans

ident = 2
json = {}
yaml = '''---
foo: "bar"
baz:
  - "qux"
  - "quxx"
corge: null
grault: 1
# gggg

garply: true
waldo: "false"
fred: "undefined"
emptyArray: []
emptyObject: {}
emptyString: ""'''

# convert string to list by new-lines
yaml_temp = yaml.split('\n')
# check if it's YAML
if yaml_temp.pop(0) != '---':
    print("It's not YAML multi-document file")
    sys.exit()

yaml = []
for i in yaml_temp:
    if not (i == '' or i.startswith('#')):
        yaml.append(i)
del yaml_temp

def spec_values():
    pass

for i in range(len(yaml)):
    if yaml[i].startswith(ident * ' ' + "- "):
        val = yaml[i].strip('- \"\'')
        json[dict_key].append(val)
    elif yaml[i] != '\n':
        pair = yaml[i].split(':')
        key = pair[0].strip('\"\' ')
        val = pair[1].strip('\"\' ')
        dict_key = key
        if len(pair[1]) == 0:
            json[key] = []
        elif val == '{}':
            json[key] = dict()
        elif val == '[]':
            json[key] = list()
        elif val.isdigit():
            json[key] = int(val)
        elif val == '\'\'' or val == '\"\"':
            json[key] = str()
        else:
            json[key] = pair[1].strip('\"\' ')

# print json
# sys.exit()

# Strings should be wrapped in double quotes
trantab = maketrans("'", '"')
print str(json).translate(trantab)
