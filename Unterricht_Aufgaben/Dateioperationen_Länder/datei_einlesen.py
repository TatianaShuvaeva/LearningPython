import os

def __get_länder_file(path_to_file) -> list[str]:
    list_länder = []
    
    with open(path_to_file, "r") as eingabe_datei:
        for zeile in eingabe_datei:
            line_neu = zeile.strip()
            list_länder.append(line_neu)

        return list_länder


def get_länder() -> list[str]:
    ordnerpfad = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path_to_file = os.path.join(ordnerpfad, "Länder.txt")
    länder = __get_länder_file(path_to_file) 
    return länder    
    