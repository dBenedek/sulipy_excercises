# https://sulipy.hu/listak/listak_bejarasa?tab=feladatok

szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]

# with enumerate:
for idx, i in enumerate(szamok):
    if i % 3 == 0 and i % 2 == 0:
        print(szamok[idx])