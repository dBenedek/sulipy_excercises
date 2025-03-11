# https://sulipy.hu/elagazasok/felteteles_vegrehajtas?tab=feladatok

felh_napja = str(input("Jo napod volt? (igen/nem)"))

if felh_napja != "igen" and felh_napja != "nem":
    print("Sajnos nem ertem a valaszodat.")
elif felh_napja == "igen":
    print("Az nagyon jo!")
else:
    print("Akkor legyen jobb.")