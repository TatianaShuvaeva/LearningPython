from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_schleimgeist import Schleimgeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_kannibalengeist import Kannibalengeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geisterjaeger import Geisterjaeger
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geisterjunge import Geisterjunge



screamer = Geist("screamer", 3)
print(screamer)

slimey = Schleimgeist("slimey", 1)
print(slimey)

bloodied_squire = Kannibalengeist("bloodied_squire", 10)
fat_manic = Kannibalengeist("fat_manic", 7)
geisterjunge = Geisterjunge("Geisterjunge", 3)
geisterjäger = Geisterjaeger("Dr. Peter Venkman")

# Geisterjäger hat screamer nicht gefangen
print('----')
print(f"Sichtbarkeitsstatus von screamer: {screamer.sichtbar}")
print(geisterjäger)
geisterjäger.geist_fangen(screamer)
print(geisterjäger)



# Geisterjäger hat fat_manic gefangen
print('----')

print(f"Sichtbarkeitsstatus von fat_manic: {fat_manic.sichtbar}")
geisterjunge.sichtbar_machen(fat_manic)
print(f"Sichtbarkeitsstatus von fat_manic: {fat_manic.sichtbar}")

print(geisterjäger)
geisterjäger.geist_fangen(fat_manic)
print(geisterjäger)

# Die  Geistersichtbarkeit erlischt

print('----')

print(f"Sichtbarkeitsstatus von bloodied_squire: {bloodied_squire.sichtbar}")
geisterjunge.sichtbar_machen(bloodied_squire)
print(f"Sichtbarkeitsstatus von bloodied_squire: {bloodied_squire.sichtbar}")

print(geisterjäger)
geisterjäger.geist_fangen(bloodied_squire)
print(f"Sichtbarkeitsstatus von bloodied_squire: {bloodied_squire.sichtbar}")
print(geisterjäger)
