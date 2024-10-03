from cl_geist import Geist
from cl_schleimgeist import Schleimgeist
from cl_kannibalengeist import Kannibalengeist


g = Geist("screamer", 3)
print(g)

s = Schleimgeist("slimey", 1)
print(s)

k = Kannibalengeist("bloodied_squire", 10)
k2 = Kannibalengeist("fat_manic", 7)

print(k)

g.spucken()
k.spucken()
k2.spucken()
s.spucken()
print(k2)
print(s)

k2.fressen(s)



