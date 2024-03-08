# Sammlung veränderbar
my_variableList = ["rot", "gelb", "grün", "rot"] # Sammlungen veränderbar
print(my_variableList)


#Sammlungen, unveränderbar
my_variableTuple = (3, 2, 1, 3)
print(my_variableTuple)

#Sammlung aber einzigartig
my_variableSet = {1, 3, 5, 7, 3}
print(my_variableSet)

# Key : Value
my_variableDict = {'name' : 'Asen' , 'alter' : '32'}
my_variableDictCustomers = {    "Kunde 1" : {'name' : 'Asen' , 'alter' : '32'},
                                "Kunde 2" : {'name' : 'Cristina' , 'alter' : '25'},
                                "Kunde 3" : {'name' : 'Petra', 'alter' : '42'}
                            }
variableBeruf = 'beruf'
my_variableDict[variableBeruf] = 'Student'
print(my_variableDictCustomers)

# if  then else Anweisung
wetterZustand = "regen"

if wetterZustand == "sonnig":
    print("Ja es ist Sonnig, Zeit zum Fahrrad fahren.")
elif wetterZustand == "regen":
    print("Denk an die Regenjacke.")
elif wetterZustand == "bewölkt":
    print("Denk an die Mütze, es ist Bewölkt.")
else:
    print("Ich habe keine Informationen zum Wetter")





my_variableSetNamen = {"Asen", "Maryam", "Michael", "Thomas", "Engin den Glatzkopf", "Engin mit Haaren", "Asen"}
print(sorted(my_variableSetNamen))