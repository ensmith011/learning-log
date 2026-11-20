def spam():
    global eggs
    eggs = 'spam'

def baccon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 'global'
spam()
print(eggs)