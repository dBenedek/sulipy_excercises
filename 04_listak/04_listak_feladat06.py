# https://sulipy.hu/listak/karakterlancok?tab=feladatok

keep_going = True
while keep_going:
    user_input = str(input("Adj meg egy mondatot (mondatvegi irasjellel, kilepes: ENTER):"))
    if user_input == "":
        keep_going = False
    else:
        if user_input[-1] == ".":
            print("Ez egy kijelento mondat.")
        elif user_input[-1] == "?":
            print("Ez egy kerdo mondat.")
        elif user_input[-1] == "!":
            print("Ez egy felkialto/ohajto mondat.")
        else:
            print("Egyeb.")
