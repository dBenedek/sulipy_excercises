# https://sulipy.hu/eljarasok_fuggvenyek/referenciak?tab=feladatok

import random

def betu_bekeres():
    """ Beker a felhasznalotol egy betut es visszaadja."""
    user_input = str(input("Találd ki, melyik ötbetűs főnévre gondoltam!\nAdj meg egy betut! "))
    return user_input

def benne_van_e(szo, betu):
    """ Eldonti, hogy a betu benne van e a szoban."""
    if betu in szo:
        return True
    else:
        return False

def tippek_frissites(tippek, valasztott_szo, betu):
    """ Frissiti a tippek nevezetu str valtozot az alapjan, hogy a megadott betu hol szerepel a valasztott_szo
        str valtozoban."""
    for idx in range(len(valasztott_szo)):
        if valasztott_szo[idx] == betu:
            tippek = tippek[:idx] + betu + tippek[idx+1:]
    return tippek

def main():
    # Alap valtozok, stb.:
    szavak = ["malac", "kalap", "tutaj", "radio", "lapat", "paraj", "malna"]
    valasztott_szo = random.choice(szavak)
    tippek = "_"*5
    rossz_tippek = list()
    probalkozasok = 0

    # Amig a felhasznalo ki nem talalja a valasztott szot:
    while "_" in tippek:
        # Betu tipp bekerese:
        betu_tipp = betu_bekeres()
        # Ha a megadott betu szerepel a valaszott szoban:
        if benne_van_e(valasztott_szo, betu_tipp):
            tippek = tippek_frissites(tippek, valasztott_szo, betu_tipp)
            print("Talalt!")
            print(f"Jelenlegi allas: {tippek}")
        # Ha a megadott betu nem szerepel a valasztott szoban:
        else:
            if betu_tipp not in rossz_tippek:
                rossz_tippek.append(betu_tipp)
            print("Sajnos nem talalt!")
            print(f"Jelenlegi allas: {tippek}")

        # Probalkozasok szama +1:
        probalkozasok += 1
        # Rossz tippek szama:
        rossz_tippek_str = ", ".join(rossz_tippek)
        print(f"Rossz tippek: {rossz_tippek_str}")
        # Dekorator:
        print("-"*80 + "\n")

    # Vege:
    print(f"Gratulalok! Kitalaltad {probalkozasok} probalkozasbol!")

# Fo fuggveny hivasa:
main()