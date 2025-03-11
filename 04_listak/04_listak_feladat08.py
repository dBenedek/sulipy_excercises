# https://sulipy.hu/listak/listak_metodusai?tab=feladatok

szinek = []

keep_going = True
while keep_going:
    input_szin = str(input("Adj meg egy szint (kilepes: ENTER):"))
    if input_szin == "":
        keep_going = False
    elif input_szin in szinek:
        print(f"Ez a szin: {input_szin} mar szerepel a listaban " + str(szinek.count(input_szin)) + "-szer")
        szinek.append(input_szin)
        print(", ".join(szinek))
    else:
        print("A megadott szin nem szerepel a listaban.")
        szinek.append(input_szin)