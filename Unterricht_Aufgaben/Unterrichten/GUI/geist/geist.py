from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_geist import Geist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_schleimgeist import Schleimgeist
from Unterricht_Aufgaben.Unterrichten.GUI.geist.geist_module.cl_kannibalengeist import Kannibalengeist


g = Geist("screamer", 3)
print(g)

s = Schleimgeist("slimey", 1)
print(s)

k = Kannibalengeist("bloodied_squire", 10)
k2 = Kannibalengeist("fat_manic", 7)

print(k)

g.spuken()
k.spuken()
k2.spuken()
s.spuken()
print(k2)
print(s)

k2.fressen(s)



