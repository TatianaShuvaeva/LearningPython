from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_schleimgeist import Schleimgeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_kannibalengeist import Kannibalengeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geisterjager import Geisterjaeger



screamer = Geist("screamer", 3, False, False)
print(screamer)

slimey = Schleimgeist("slimey", 1, False, False)
print(slimey)

bloodied_squire = Kannibalengeist("bloodied_squire", 10, False, False)
fat_manic = Kannibalengeist("fat_manic", 7, False, False)

geisterjäger = Geisterjaeger("geisterjäger", 7, False, False)
geisterjäger.geist_fangen(screamer)

# print(bloodied_squire)

# screamer.spuken()
# bloodied_squire.spuken()
# fat_manic.spuken()
# slimey.spuken()
# print(fat_manic)
# print(slimey)

# fat_manic.fressen(slimey)





