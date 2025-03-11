# https://sulipy.hu/adattipusok/szotar?tab=feladatok

macska_adatok = {}

def adat_bekeres():
    nev = input("Add meg a macska nevet: ")
    kor = int(input("Add meg a macska korat: "))
    return nev, kor

def adat_valtoztatas(valt_param, uj_ertek):
    macska_adatok[valt_param] = uj_ertek

macska_nev, macska_kor = adat_bekeres()
macska_adatok["nev"] = macska_nev
macska_adatok["kor"] = macska_kor

print(macska_adatok)

param_mod = input("Ird le a megvaltozatni kivant parameter nevet: ")
uj_ertek = input("Add ennek az uj erteket: ")
macska_adatok[param_mod] = uj_ertek

print(macska_adatok)