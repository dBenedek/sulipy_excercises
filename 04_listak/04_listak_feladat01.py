# https://sulipy.hu/listak/listak_letrehozasa?tab=feladatok

keep_going = True
names = list()
while keep_going:
    name = str(input("Adj meg egy nevet vagy nyomj ENTER-t befejezeshez: "))
    names.append(name)
    if name == "":
        keep_going = False
print("A nevek amiket megadtal: "+" ".join(names))
