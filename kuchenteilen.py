a=int(input())
b=int(input())
d=1
while True:
    if d%a==0 and d%b==0:
        break 
    d += 1

print(d)  
