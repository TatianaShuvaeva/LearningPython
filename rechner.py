a=float(input())
b=float(input())
c=str(input())
if c == '+':
    print(a+b)
   
elif c=='-':
    print(a-b)
  
elif a!=0 and b!=0 and c=='/':
    print(a/b)
  
   
elif c=='*':
    print(a*b)
  
elif a!=0 and b!=0 and c=='mod':
    print(a%b)
  
elif  c=='pow':
    print(a**b)
 
elif a!=0 and b!=0 and c=='div':
    print(a//b)
else:
    print('Деление на 0!')