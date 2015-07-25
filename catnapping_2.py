spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

#print(spam.split('\n'))

def printPicnic(string, test=[]):
    test.append(string)
    return(test)

print(printPicnic('test'))
print(printPicnic('test2'))
