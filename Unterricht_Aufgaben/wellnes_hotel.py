eingabe_wellness = str(input("Willst Du Wellness-Komplettpaket. Gib bitte ja oder nein ein: "))
eingabe_drei_uebernachtungen = str(input("Willst Du drei oder mehr Übernachtungen. Gib bitte ja oder nein ein: "))
eingabe_vollpension = str(input("Willst Du Vollpension. Gib bitte ja oder nein ein: "))

if eingabe_wellness == 'ja' and eingabe_drei_uebernachtungen == 'ja' and eingabe_vollpension == 'ja':
    print("Früstück mit Abendbrot, Mittagessen, 5 Freigetränke, freie Nutzung des Fitnessraums, Saunabesuch gratis, eine Massage gratis  gebucht")

elif eingabe_wellness == 'ja' and eingabe_drei_uebernachtungen == 'ja' and eingabe_vollpension == 'nein':
    print("Früstück mit Abendbrot, 5 Freigetränke, freie Nutzung des Fitnessraums, Saunabesuch gratis, eine Massage gratis  gebucht")
    
elif eingabe_wellness == 'ja' and eingabe_drei_uebernachtungen == 'ja' and eingabe_vollpension == 'nein':
    print("Früstück mit Abendbrot, 5 Freigetränke, freie Nutzung des Fitnessraums, Saunabesuch gratis, eine Massage gratis  gebucht")

elif eingabe_wellness == 'ja' and eingabe_drei_uebernachtungen == 'nein' and eingabe_vollpension == 'ja':
    print("Früstück mit Abendbrot, Mittagessen, 5 Freigetränke, freie Nutzung des Fitnessraums, Saunabesuch gratis, eine Massage gratis  gebucht")
    
elif eingabe_wellness == 'ja' and eingabe_drei_uebernachtungen == 'nein' and eingabe_vollpension == 'nein':
    print("Früstück mit Abendbrot, 5 Freigetränke, freie Nutzung des Fitnessraums, Saunabesuch gratis, eine Massage gratis  gebucht")

elif eingabe_wellness == 'nein' and eingabe_drei_uebernachtungen == 'ja' and eingabe_vollpension == 'ja':
    print("Früstück mit Abendbrot, Mittagessen, 5 Freigetränke, freie Nutzung des Fitnessraums, Saunabesuch gratis gebucht")

elif eingabe_wellness == 'nein' and eingabe_drei_uebernachtungen == 'ja' and eingabe_vollpension == 'nein':
    print("Früstück mit Abendbrot, freie Nutzung des Fitnessraums, Saunabesuch gratis  gebucht")

elif eingabe_wellness == 'nein' and eingabe_drei_uebernachtungen == 'nein' and eingabe_vollpension == 'ja':
    print("Früstück mit Abendbrot, Mittagessen, 5 Freigetränke, freie Nutzung des Fitnessraums  gebucht")
    
elif eingabe_wellness == 'nein' and eingabe_drei_uebernachtungen == 'nein' and eingabe_vollpension == 'nein':
    print("Früstück mit Abendbrot, Mittagessen, 5 Freigetränke, freie Nutzung des Fitnessraums  gebucht")


