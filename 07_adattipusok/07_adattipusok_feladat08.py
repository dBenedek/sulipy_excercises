# https://sulipy.hu/adattipusok/szotar_gyakorlatban?tab=feladatok

def main():
    konyvtar = []
    while True:
        szerzo = input("Add meg a konyv szerzojet: ")
        if szerzo == "":
            break
        cim = input("Add meg a konyv cimet: ")
        konyvtar.append({"szerzo":szerzo, "cim":cim})
    print(konyvtar)

main()
