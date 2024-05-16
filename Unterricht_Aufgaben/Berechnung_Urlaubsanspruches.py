#Aufgabe 1

# behinderung = int(input("Geben Sie bitte ein, wie viel Prozent beträgt die Behinderung: "))
# alter_beschaeftigten = int(input("Geben Sie bitte Alter der Beschäftigte ein: "))
# urlaub = 30


# if behinderung >= 50:
#     urlaub +=   5 
# else:    
    
#     if alter_beschaeftigten < 18:
#         urlaub = 35
    
#     else:
#         if alter_beschaeftigten > 55: # alter_beschaeftigten >= 55 muss sein
#             urlaub = 32
#         else:
#             urlaub = 30         


# print(urlaub)


#Aufgabe 2

# behinderung = int(input("Geben Sie bitte ein, wie viel Prozent beträgt die Behinderung: "))
# alter_beschaeftigten = int(input("Geben Sie bitte Alter der Beschäftigte ein: "))
# urlaub = 30

# if alter_beschaeftigten >18:  # alter_beschaeftigten >=18 muss sein
      
#     if alter_beschaeftigten < 55:
#         urlaub = 30 
#     else:
#         urlaub = 32         
# else:
#     urlaub = 35        


# if behinderung > 50:  #behinderung >=50 muss sein
#     urlaub +=  5
     
# print(urlaub)


#Aufgabe 3

behinderung = int(input("Geben Sie bitte ein, wie viel Prozent beträgt die Behinderung: "))
alter_beschaeftigten = int(input("Geben Sie bitte Alter der Beschäftigte ein: "))
urlaub = 30

if alter_beschaeftigten > 55: # alter_beschaeftigten >= 55 muss sein
        urlaub = 32
else:
    if alter_beschaeftigten < 18:
        urlaub = 35
    else:
        urlaub = 30  
      

if behinderung >= 50:
    urlaub +=  5
     
print(urlaub)


#Aufgabe 4

# behinderung = int(input("Geben Sie bitte ein, wie viel Prozent beträgt die Behinderung: "))
# alter_beschaeftigten = int(input("Geben Sie bitte Alter der Beschäftigte ein: "))
# urlaub = 30

# if alter_beschaeftigten < 18:
#    urlaub = 35 

# if alter_beschaeftigten <= 55: # alter_beschaeftigten < 55 muss sein, 
#                                # fälschlicherweise für alle Beschäftigte unter 18 Jahren berechnet, urlaub= 30 wird sein
#     urlaub = 30 
# else:
#     urlaub = 32
     
# if behinderung >= 50:
#     urlaub +=  5
     
# print(urlaub)
