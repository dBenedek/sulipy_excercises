# https://sulipy.hu/listak/listak_bejarasa?tab=feladatok

szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

szavak_t = list()
for i in szavak:
    if i[0].upper() == "T":
        szavak_t.append(i)
print(szavak_t)
