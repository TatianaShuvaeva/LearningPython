a=int(input())
b=int(input())
c=int(input())
if b<=a>=c:
    max=a
    print(max)
elif a <= b >= c:
    max=b
    print(max)
else :
    max=c
    print(max)
if b>=a<=c:
    min=a
    print(min)
elif a>=b<=c:
    min=b
    print(min)
else:
    min=c
    print(min)
avg=a+b+c-max-min
print(avg)