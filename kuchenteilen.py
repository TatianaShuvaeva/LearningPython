a=int(input())
b=int(input())
d=1
while not (d%a==0 and d%b==0):
    d += 1

print(d)  
