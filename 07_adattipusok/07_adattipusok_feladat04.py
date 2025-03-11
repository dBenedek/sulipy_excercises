# https://sulipy.hu/adattipusok/szotar?tab=feladatok

kutya_neve = str(input("Add meg a kutya nevet: "))
kutya_eletkora = int(input("Add meg a kutya eletkorat: "))
kutya_fajta = str(input("Add meg a kutya fajtajat: "))
kutya_oltas = str(input("Rendelkezik a kutya ervenyes oltassal veszettseg ellen? "))

kutya_adatok = {"nev":kutya_neve, "kor":kutya_eletkora,
                "fajta":kutya_fajta, "oltas":kutya_oltas}

print(kutya_adatok)