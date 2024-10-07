from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_schleimgeist import Schleimgeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_kannibalengeist import Kannibalengeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geisterjager import Geisterjaeger



screamer = Geist("screamer", 3)
print(screamer)

slimey = Schleimgeist("slimey", 1)
print(slimey)

bloodied_squire = Kannibalengeist("bloodied_squire", 10)
fat_manic = Kannibalengeist("fat_manic", 7)

geisterjäger = Geisterjaeger("Dr. Peter Venkman")
print(geisterjäger)
screamer.sichtbar = True
print(f"gefangen: {geisterjäger.geist_fangen(screamer)}")
print(geisterjäger)
# print(bloodied_squire)

# screamer.spuken()
# bloodied_squire.spuken()
# fat_manic.spuken()
# slimey.spuken()
# print(fat_manic)
# print(slimey)

# fat_manic.fressen(slimey)





