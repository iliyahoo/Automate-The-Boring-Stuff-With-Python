#!/usr/bin/python

import sys, re, urllib2, string

ident = 2 # set identation
num = re.compile(r'\d+\.?\d*') # compile cypher-like regex
strip_out = '\"\' ' # strip out quotes and white-spaces

# for test purpose
yaml_temp = '''---
foo: "bar"
baz:
  - "qux"
  - "quxx"
corge: null
grault:
  garply: true
waldo: "false"
fred: "undefined"
emptyArray: []
emptyObject: {}
emptyString: ""'''

## open an URL
#response = urllib2.urlopen('https://gist.githubusercontent.com/dmitrypa/ee74d809505bf6c69f6f/raw/01e84c2bcb791153346b57cca4e4d2751b8ca111/example.yml')
#yaml_temp = response.read()

# convert string to list delimited by new-lines
yaml_temp = yaml_temp.split('\n')
# check if it's YAML
if yaml_temp.pop(0) != '---':
    print("It's not YAML multi-document file")
    sys.exit()

# wipe out comments and empty lines
yaml = []
for i in yaml_temp:
    if not (i == '' or i.startswith('#')):
        yaml.append(i)
del yaml_temp

json = {}
# iterate over list
for i in range(len(yaml)):
    # it's the list element if indented and started with '- '
    if yaml[i].startswith(ident * ' ' + "- "):
        val = yaml[i].strip('-' + strip_out)
        json[dict_key].append(val) # append to anchored dict key
    elif yaml[i].startswith(ident * ' '): # nested dict
        val = yaml[i].strip(strip_out)
        dict_key = json[dict_key]
        print dict_key
    else: # create item in the json dict
        pair = yaml[i].split(':')
        key = pair[0].strip(strip_out)
        val = pair[1].strip(strip_out)
        dict_key = key # anchor for last created dict key containing empty list
        if len(val) == 0:
            json[key] = []
        elif val == '{}': # preserve dictionary type
            json[key] = dict()
        elif val == '[]': # preserve list type
            json[key] = list()
        elif num.search(val): # preserve int or float type
            if float(val) % 1 == 0:
                val = int(val)
            else:
                val = float(val)
            json[key] = val
        elif val == '\'\'' or val == '\"\"': # preserve string type
            json[key] = str()
        else:
            json[key] = val

# Strings should be wrapped in double quotes
trantab = string.maketrans("'", '"') # create translation table
json = str(json).translate(trantab)

# print out to the file
with open('gett.json', 'w') as file:
    file.write(json)
