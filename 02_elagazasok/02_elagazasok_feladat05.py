# https://sulipy.hu/elagazasok/logikai_kifejezesek?tab=feladatok

kerdes_01 = str(input("Henrik jon ma kosarazni? (igen/nem)"))
kerdes_02 = str(input("Hanna jon ma kosarazni? (igen/nem)"))

if kerdes_01 == "nem" and kerdes_02 == "nem":
    print("Egyikuk sem jon kosarazni.")
elif (kerdes_01 == "igen" and kerdes_02 == "nem") or (kerdes_02 == "igen" and kerdes_01 == "nem"):
    print("Egyikuk jon csak kosarazni.")
elif kerdes_01 == "igen" and kerdes_02 == "igen":
    print("Mindketten jonnek kosarazni.")
else:
    print("Egyeb.")