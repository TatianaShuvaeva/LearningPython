# List Comprehension = Liste - Abstraktion

zahlen = [2,34, -56.6, -12.4, 67.9]


pos_zahlen = [z for z in zahlen if z > 0]
print(pos_zahlen)

text ="Python ist eine Programmiersprache"


vokale = [v for v in text if v in "aeiou"]
print(vokale)

vokale = {v for v in text if v in "aeiou"}
print(vokale)