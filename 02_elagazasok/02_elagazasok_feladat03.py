# https://sulipy.hu/elagazasok/felteteles_vegrehajtas?tab=feladatok

import random

rand_szam = random.randint(1, 5)
input_szam = int(input("Adj meg egy egesz szamot 1 es 5 kozott."))

if input_szam < 1 or input_szam > 5:
    print("1 es 5 kozott adhatsz meg csak.")
elif input_szam == rand_szam:
    print("Eltalaltad a helyes szamot!")
elif input_szam < rand_szam:
    print("A helyes szam ennel nagyobb.")
else:
    print("A helyes szam ennel kisebb.")