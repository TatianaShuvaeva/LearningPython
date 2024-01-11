def get_leerzeichen(wort) -> str:
    wort_len = len(wort)
    anzahl_links = 70-wort_len
    leerzeichen = " " * anzahl_links
    ergebniss = leerzeichen + wort
    return ergebniss


str = 'blblblblb'
ergebniss1 = get_leerzeichen(str)
print(ergebniss1)

str = 'allen'
ergebniss2 = get_leerzeichen(str)
print(ergebniss2)

# def ridht_justify(str):
#     pro=" "*(70-len(str))
#     justify=pro+str

# str='allen'
# ridht_justify(justify)


# def print_zweimal(str):
#     print(str)
#     print(str)

# def zweimal_cat(teil1,teil2):
#     cat = teil1 + " " + teil2
#     print_zweimal(cat)

# zeile1="Hallo Welt"
# zeile2="from Tatiana"
# zweimal_cat(zeile1,zeile2)
