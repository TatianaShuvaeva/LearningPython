if True == False:
    print('crazy')
    
a = ['dog', 'cat']
b = a
print(id(a) == id(b)) # True

b = ['dog', 'cat']
print(id(a) == id(b)) #False
