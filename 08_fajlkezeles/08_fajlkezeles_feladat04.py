# https://sulipy.hu/fajlkezeles/json?tab=feladatok

import json

forrasfajl = open('/home/benedek_danko/PycharmProjects/sulipy_excercises/data/lista.txt')
sorok = list(i.strip() for i in forrasfajl.readlines())
forrasfajl.close()

sorok_szotar = []
for i in range(0, len(sorok)-4, 5):
    elem = {"datum": sorok[i],
            "sorozat": sorok[i+1],
            "epizod": sorok[i+2],
            "hossz": int(sorok[i+3]),
            "latta": bool(int(sorok[i+4]))}
    sorok_szotar.append(elem)

with open('/home/benedek_danko/PycharmProjects/sulipy_excercises/data/lista.json', 'w',
          encoding='utf-8') as celfajl:
    json.dump(sorok_szotar, celfajl, indent=2)
celfajl.close()
