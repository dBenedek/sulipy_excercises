# https://sulipy.hu/eljarasok_fuggvenyek/referenciak?tab=feladatok

import random

def szam_beker():
    user_input = int(input("Adj meg egy egesz szamot (kilepes 0-val): "))
    return user_input

def main():
    veletlen_szam = random.randrange(1, 11)
    while veletlen_szam != 0:
        veletlen_szam = szam_beker()

main()
