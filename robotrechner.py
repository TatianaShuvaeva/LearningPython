n=int(input())
sum=n%10
sum2=n%100
if n==0:
    print(n,' программистов')
elif sum==0:
    print(n,' программистов')
elif 5<=n<=19:
    print(n,' программистов')
elif 5<=sum<=9:
    print(n,' программистов')
elif 11<=sum2<=14: 
     print(n,' программистов')
elif n==1: 
    print(n,' программист')
elif sum==1:
   print(n,' программист')
else:
    print(n,' программиста')