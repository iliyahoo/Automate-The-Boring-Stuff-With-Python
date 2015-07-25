#!/usr/bin/python

import sys, string

strip_out = '-:\"\' ' # strip out quotes, white-spaces, colon and dash

# for test purpose
yaml_temp = '''---
foo: "bar"
baz:
  - "qux"
  - "quxx"
corge: null
grault: 1
garply: true
waldo: "false"
fred: "undefined"
emptyArray: []
emptyObject: {}
emptyString: ""
strakovich:
  iliya:
    - 328800065
    - 1975'''

## open an URL
#response = urllib2.urlopen('https://gist.githubusercontent.com/dmitrypa/ee74d809505bf6c69f6f/raw/01e84c2bcb791153346b57cca4e4d2751b8ca111/example.yml')
#yaml_temp = response.read()

# convert string to list delimited by new-lines
yaml = yaml_temp.split('\n')
# check if it's YAML
if yaml.pop(0) != '---':
    sys.exit()

# wipe out comments and empty lines
yaml = []
for i in yaml_temp:
    if not (i == '' or i.startswith('#')):
        yaml.append(i)
del yaml_temp

json = []
for index in range(len(yaml)):
    item = yaml[index].split(':')
    key = item[0].strip(strip_out)
    # add list
    if len(item) == 1:
        json[anchor] += '"' + key + '"' + ', '
    # add key
    elif len(item) == 2 and len(item[1]) == 0:
        try:
            json[anchor] += '"' + key + '"' + ':'
        except:
            json.append('"' + key + '"' + ':')
            anchor = len(json) - 1
    # add whole item
    else:
        val = item[1].strip(strip_out)
        val = '"' + val + '"'
        json.append('"' + key + '"' + ':' + val)
        try:
            del anchor
        except:
            continue

for ind in range(len(json)):
    if json[ind].endswith(', '):
        lst = json[ind].split(':')
        mod_list = lst[:-1]
        lst[-1] = '[' + lst[-1].rstrip(', ') + ']'
        json[ind] = ':'.join(lst)
#    elif json[ind].count(':') >= 2:
#        print json[ind]

# Strings should be wrapped in double quotes
trantab = string.maketrans("'", ' ') # create translation table
json = str(json).translate(trantab)

print '{ ' + json.strip('[ ]') + '] }'

## print out to the file
#with open('gett.json', 'w') as file:
#    file.write(json)
