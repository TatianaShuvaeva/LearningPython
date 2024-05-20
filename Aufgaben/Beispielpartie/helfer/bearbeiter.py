from io import TextIOWrapper


class Bearbeiter:
    def verarbeiten_file(file_input: TextIOWrapper):
        
        metadaten = {}
        zuege_spiel = []

        games = ''
        line = file_input.readline()
        while line != '\n':
            line_neu = line.strip('][\n') #Entfernt man eckige Klammern und Zeilenumbrüche
            line_split = line_neu.split(' ', maxsplit=1) #Teilt man die Zeichenfolge mit Leerzeichen als Trennzeichen auf
            key = line_split[0]
            value = line_split[1].strip('"')
            metadaten[key] = value
            line = file_input.readline()          
        
        while line != '':        
            line = file_input.readline()
            games_ohne = line.strip('\n')  # Entfernt man Zeilenumbrüche
            
            # Fügt man die Zeilen zu einer zusammen und fügt man ein Leerzeichen
            # dazwischen ein'
            games = games + ' ' + games_ohne
        
        games_split = games.split()  # Teilt man eine Zeile mit einem Leerzeichen

        games_refined = []
        for element in games_split[:-1]:  # Alle Elemente außer dem letzten
            for symbol in element:
                if symbol.isdigit() is True:  # Überprüft man, ob es Ziffern in jedem Element gibt
                    games_refined.append(element)  # Entfernt man {Kasparov schüttelt kurz den Kopf}
                    break
            
        for element in games_refined:
            igames_element = element.split('.')  # Element nach Punkt aufteilen
            
            #  Fügt man dem neuen Array nur zweite Element hinzu, wenn es zwei davon gibt
            
            if len(igames_element) == 2:
                zuege_spiel.append(igames_element[1]) 
            else:
                zuege_spiel.append(igames_element[0])
        
        print(metadaten)
        
        # for element in zuege_spiel:
        #     print(f"zuege[{zuege_spiel.index(element)}]={element}")

        for idx, element in enumerate(zuege_spiel):  # Zweite bessere Variante 
            print(f"zuege[{idx}]={element}")