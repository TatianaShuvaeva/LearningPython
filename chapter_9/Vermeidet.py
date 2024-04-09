def vermeidet(wort, vervotenBuchstaben) -> str:
    for letter in wort:
        if letter in vervotenBuchstaben: 
            return False
    return True


print(vermeidet('Sehenswürdigkeiten', 'azlxmb'))