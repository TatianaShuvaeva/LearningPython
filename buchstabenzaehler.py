s=input()
a=s.count('g') 
b=s.count('C') 
d=s.count('G') 
e=s.count('c')
sum=a+b+d+e
dl=len(s)
print((sum/dl)*100)