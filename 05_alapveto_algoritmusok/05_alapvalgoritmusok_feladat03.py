# https://sulipy.hu/alapveto_algoritmusok/kereses?tab=feladatok

import random

szamok = [random.randrange(1, 8) for x in range(5)]
user_input = int(input("Adj meg egy egesz szamot: "))
if user_input in szamok:
    print("Ez a szam szerepel a listaban.")
else:
    print("Ez a szam nem szerepel a listaban.")
print(szamok)