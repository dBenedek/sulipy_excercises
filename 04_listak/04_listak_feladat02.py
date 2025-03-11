# https://sulipy.hu/listak/listak_letrehozasa?tab=feladatok

import random

rand_nums = [random.randrange(0, 51) for x in range(10) if x % 4 == 0]
print(rand_nums)
print("Lista hossza:", len(rand_nums))