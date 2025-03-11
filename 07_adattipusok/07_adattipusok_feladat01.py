# https://sulipy.hu/adattipusok/listakat_tartalmazo_listak?tab=feladatok

import random

tarolo = [[random.randrange(0, 26) for x in range(3)] for y in range(4)]

for i in tarolo:
    print(i)