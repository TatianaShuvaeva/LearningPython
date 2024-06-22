# a = ([1,2,3], 20, 30)

# b = a
# print(a is b) 
# print(id(a))
# print(id(b))


# a[0][0] = 42
# print(a) # ([42,2,3], 20, 30)
# print(b) # ([42,2,3], 20, 30)

# print('------------------------')

# a = ([1,2,3], 20, 30)
# b = ([1,2,3], 20, 30)

# print(a is b) 
# print(id(a))
# print(id(b))

# print(a == b)

# print('------------------------')

richtige_nummer = 1
print(id(richtige_nummer))

nummer = 1 #int(input())
print(id(nummer))

print(richtige_nummer == nummer)
print(richtige_nummer is nummer)
