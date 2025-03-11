# https://sulipy.hu/listak/listak_metodusai?tab=feladatok

szinek = []

keep_going = True
while keep_going:
    input_szin = str(input("Adj meg egy szint (kilepes: ENTER):"))
    if input_szin == "":
        keep_going = False
    elif input_szin in szinek:
        print(f"Ez a szin: {input_szin} mar szerepel a listaban")
        print(", ".join(szinek))
    else:
        szinek.append(input_szin)
