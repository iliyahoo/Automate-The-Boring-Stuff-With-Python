def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a localw

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
ham()
spam()
print(eggs)
