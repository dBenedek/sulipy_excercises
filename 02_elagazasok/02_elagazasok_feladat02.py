# https://sulipy.hu/elagazasok/felteteles_vegrehajtas?tab=feladatok

input_szam = int(input("Adj meg egy szamot: "))

if input_szam == 0:
    print("Se nem paros, se nem paratlan.")
elif input_szam % 2 == 0:
    print("Ez egy paros szam.")
else:
    print("Ez egy paratlan szam.")