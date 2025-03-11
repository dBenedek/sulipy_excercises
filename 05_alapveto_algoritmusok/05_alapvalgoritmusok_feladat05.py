# https://sulipy.hu/alapveto_algoritmusok/kereses?tab=feladatok

# Torpedo jatek

import random

print("-"*80)
print("Ez egy torpedojatek.")
print("Tippelj a 3x3-as tablan, hogy hol lehet az egy egysegnyi hajo. Pl. B2 vagy C1.")
print("-"*80)

poz_x_ossz = ["A", "B", "C"]
hajo_poz_x = random.choice(poz_x_ossz)
hajo_poz_y = str(random.randrange(1, 4))

talalt = False
probalkozasok = 0
while not talalt:
    user_guess = str(input("Tippeld meg a hajo poziciojat (kilepes: ENTER): "))
    probalkozasok += 1
    if user_guess == "":
        talalt = True
        print("Kilepes...")
    elif (user_guess[0] == hajo_poz_x) and (user_guess[1] == hajo_poz_y):
        print("Eltalaltad!")
        print(f"Probalkozasok szama: {probalkozasok}")
        talalt = True
    else:
        print("Nem talalt!")



print(f"A hajo pozicioja: {hajo_poz_x + hajo_poz_y}")

print("-"*80)
print("Vege.")
print("-"*80)