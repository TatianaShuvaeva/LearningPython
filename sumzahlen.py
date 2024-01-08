s=[int(i) for i in input().split()]
sum = 0
for i in range(len(s)):                  
    if i==0 and len(s)-1>=1:             
        sum = s[i+1] + s[-1]                 
    elif i==len(s)-1 and len(s)-1>=1:    
        sum = s[i-1] + s[0]                  
    elif len(s)==1:                      
        sum = s[i]                           
    else:                                
        sum = s[i-1] + s[i+1]                
    print(sum, end=" ")
 