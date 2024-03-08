def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res


print(my_range(2, 5))
print(my_range(2, 15, 3))
print(my_range(15, 2, -3))

# def min(*a):
#     m=a[0]
#     for x in a:
#         if m>x:
#             m=x
#     return m

# print(min(5))
# print(min(5,3))
# print(min(5,3,6,10))
# print(min([5,3,6,10]))
