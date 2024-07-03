dc = {1: 31, 2:"FG_", "Werner":31}
print(dc)

k = dc.keys()
print(k)

for schluessel in k:
    print(schluessel)
if 1 in k:
    print("Schlüssel 1 ist enthalten")

v = dc.values()
print(v)

for wert in v:
    print(wert)
if 31 in v:
    print("Wert 31 ist enthalten")
i = dc.items()
print(i)

for k,v in i:
    print(f"Schlüssel {k}, Wert {v}")