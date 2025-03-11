# https://sulipy.hu/listak/listak_metodusai?tab=feladatok

import random

rand_szamok = [random.randrange(1, 4) for x in range(10)]
print(rand_szamok)

user_input = int(input("Adj meg egy szamot [1;3] intervallumban: "))

while user_input in rand_szamok:
    rand_szamok.remove(user_input)
print(rand_szamok)
