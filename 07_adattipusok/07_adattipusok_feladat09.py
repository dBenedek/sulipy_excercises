# https://sulipy.hu/adattipusok/szotar_gyakorlatban?tab=feladatok

'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('/home/benedek_danko/PycharmProjects/Sulipy/autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

legoregebb_auto = max(autok, key=lambda auto: auto["kor"])

print("-"*20 + " 1. feladat " + "-"*20)
print(f"A legoregebb auto: {legoregebb_auto['rendszam']}, {legoregebb_auto['marka']} {legoregebb_auto['tipus']}, {legoregebb_auto['kor']} eves.")

megjavitott_autok = list(filter(lambda auto: auto["javitva"] == True, autok))

print("-"*20 + " 2. feladat " + "-"*20)
print("A mar megjavitott autok rendszama:")
for auto in megjavitott_autok:
    print(auto["rendszam"])

print("-"*20 + " 3. feladat " + "-"*20)
atl_jav_kolt = sum(list(map(lambda auto: auto["koltseg"], autok))) / len(autok)
print(f"Az egy autora juto atlagos javitasi koltseg: {atl_jav_kolt} Ft.")

print("-"*20 + " 4. feladat " + "-"*20)
megadott_rendszam = input("Adjon meg egy rendszamot (pl. ABC-123): ")
rendszamok = list(map(lambda auto: auto["rendszam"], autok))
if megadott_rendszam in rendszamok:
    print("A megadott rendszamu auto a muhelyben van.")
else:
    print("A megadott rendszamu auto nincs a muhelyben.")

print("-"*20 + " 5. feladat " + "-"*20)
megadott_betu = input("Adjon meg egy betut: ")
osszes_marka_tipus = list(map(lambda auto: auto["marka"] + " " + auto["tipus"], autok))
osszes_marka_tipus_filt = list(filter(lambda auto: megadott_betu.lower() in auto.lower(), osszes_marka_tipus))
if len(osszes_marka_tipus_filt) > 0:
    print(f"A megadott betu az alabbi marka- vagy tipusmegnevezesekben fordul elo:\n{', '.join(osszes_marka_tipus_filt)}")