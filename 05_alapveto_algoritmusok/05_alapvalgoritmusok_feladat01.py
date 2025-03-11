# https://sulipy.hu/alapveto_algoritmusok/osszegzes?tab=feladatok

import random

szamok = [random.randrange(1, 11) for x in range(5)]

osszeg = 0
for i in szamok:
    if i % 2 == 0:
        osszeg += i
print(osszeg)
print(szamok)