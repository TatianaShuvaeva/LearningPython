# Aufgabe 1 Fahrenheit in Celsius

# fahrenheit = [12,45,67, 89]
  
# celsius = list(map((lambda i: (i-32) * 5/9), fahrenheit))
# for i in celsius:
#     print(round(i))
 
# Aufgabe 2 Celsius in Fahrenheit  
# celsius = [12,45,67, 89]
  
# fahrenheit = list(map(lambda i: (i * 9/5)+32, celsius))
# for k in fahrenheit:
#     print(round(k))
    
# Aufgabe 3 Listenabstraktion (List Comprehension)

# fahrenheit = [12,45,67, 89]
  
# celsius = list(map((lambda i: (i-32) * 5/9), fahrenheit))
    
# liste_celsius = [round(v) for v in celsius]
# print(liste_celsius)


# Aufgabe 4 Listenabstraktion (List Comprehension)

celsius = [12,45,67, 89]
  
fahrenheit = list(map(lambda i: (i * 9/5)+32, celsius))
liste_fahrenheit = [round(v) for v in fahrenheit]
print(liste_fahrenheit)