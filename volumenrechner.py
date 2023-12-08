V=str(input())
if V =='треугольник':
    a=float(input())
    b=float(input())
    c=float(input())
    p=(a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**(0.5))
elif V=='прямоугольник':  
    a=float(input())
    b=float(input())
    print(a*b)
else:
    
    r=float(input())
    P=3.14
    print(P*r**2)