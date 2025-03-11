# https://sulipy.hu/elagazasok/logikai_kifejezesek?tab=feladatok

input_szam = int(input("Adj meg egy egesz szamot: "))

if input_szam > 0 and input_szam % 2 == 0:
    print("Ez egy pozitiv paros szam.")
elif input_szam < 0 and input_szam % 2 != 0:
    print("Ez egy negativ paratlan szam.")
else:
    print("Egyeb.")