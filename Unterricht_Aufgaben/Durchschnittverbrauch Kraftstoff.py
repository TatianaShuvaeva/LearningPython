# kraftstoffmenge = float(input("Bitte geben Sie die kraftstoffmenge ein: "))
# kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))

# durchschnittverbrauch = (kraftstoffmenge/kilometer) * 100

# print(f"Durchschnittverbrauch:{durchschnittverbrauch} Liter/100 km")

richtig_eingeben = False
Versuchen = 1 
kraftstoffmenge = float(input("Bitte geben Sie die Kraftstoffmenge ein: "))
kilometer = float(input("Bitte geben Sie die gefahrenen Kilometer ein: "))
while Versuchen > 0:
   
    if kraftstoffmenge > 0:        
       
        if  kilometer > 0:            
            durchschnittverbrauch = round((kraftstoffmenge/kilometer) * 100)
            print(f"Durchschnittverbrauch: {durchschnittverbrauch} Liter/100 km")
            richtig_eingeben = True
            break
        else:
            print(f"Die gefahrene Kilometer sollte > 0 sein")
            kilometer = float(input("Bitte geben Sie noch mal die gefahrenen Kilometer ein: "))        
    else:    
        print(f"Die Kraftstoffmenge sollte > 0 sein")
        kraftstoffmenge = float(input("Bitte geben Sie noch mal die Kraftstoffmenge ein: "))


    

