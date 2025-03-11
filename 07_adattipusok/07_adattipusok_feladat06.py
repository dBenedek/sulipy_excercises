# https://sulipy.hu/adattipusok/szotar?tab=feladatok

adatok = {"nev":"Danko Benedek",
          "kor":28,
          "magyar":True}

def adatot_hozzaad(kulcs, ertek):
    adatok[kulcs] = ertek

def main():
    print(adatok)
    while True:
        uj_kulcs = input("Adj meg egy uj kulcsot (kilepes: ENTER): ")
        if uj_kulcs == "":
            break
        uj_ertek = input("Add meg az uj kulcshoz tartozo erteket (kilepes: ENTER): ")
        if uj_ertek == "":
            break
        adatot_hozzaad(uj_kulcs, uj_ertek)
        print(adatok)

main()