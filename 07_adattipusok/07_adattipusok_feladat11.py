# https://sulipy.hu/adattipusok/halmaz?tab=feladatok

import random

random_szamok = set(random.sample(range(10), 5))

while True:
    megadott_szamok = input("Adj meg 5 szamot vesszovel elvalasztva, space nelkul (kilepes: ENTER): ")
    if megadott_szamok == "":
        break
    megadott_szamok = set(int(i) for i in megadott_szamok.split(","))
    eltalalt_szamok = random_szamok & megadott_szamok
    nem_talalt_szamok = random_szamok - megadott_szamok
    rogzitett_szamok = random_szamok | megadott_szamok
    nem_rogzitett_szamok = set(range(10)) - rogzitett_szamok
    print(f"{len(eltalalt_szamok)} szamot talaltal el: {', '.join(list(str(i) for i in eltalalt_szamok))}")
    print(f"{len(nem_talalt_szamok)} szamot nem talaltal el: {', '.join(list(str(i) for i in nem_talalt_szamok))}")
    print(f"Rogzitett szamok: {', '.join(list(str(i) for i in rogzitett_szamok))}")
    print(f"Nem rogzitett szamok: {', '.join(list(str(i) for i in nem_rogzitett_szamok))}")

random.random()