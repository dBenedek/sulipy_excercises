# https://sulipy.hu/eljarasok_fuggvenyek/scope?tab=feladatok

import random



def eltalalta(aktualis_tipp, elt_szam):
    if aktualis_tipp == elt_szam:
        return True
    else:
        return False

def tipp_bekero():
    user_input = int(input("Tippelj egy egesz szamot: "))
    return user_input

def main():
    tippek_szama=0
    kitalalando = random.randrange(1, 11)
    while True:
        tipp = tipp_bekero()
        tippek_szama += 1
        if eltalalta(tipp, kitalalando):
            print(f"Gratulalok, eltalaltad {tippek_szama} probalkozasbol.")
            break
        else:
            print(f"Nem talaltad el. Ez volt a {tippek_szama}. probalkozasod.")

main()