# Fahrenheit in Celsius

# fahrenheit = [12,45,67, 89]
  
# celsius = list(map((lambda i: (i-32) * 5/9), fahrenheit))
# for i in celsius:
#     print(round(i))
 
# Celsius in Fahrenheit  
celsius = [12,45,67, 89]
  
fahrenheit = list(map(lambda i: (i * 9/5)+32, celsius))
for k in fahrenheit:
    print(round(k))