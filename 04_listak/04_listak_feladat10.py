# https://sulipy.hu/listak/listak_metodusai?tab=feladatok

betuk = list()

keep_going = True
while keep_going:
    user_input = str(input("Adj meg egy betut (kilepes: ENTER): "))
    if user_input == "":
        keep_going = False
    elif user_input.upper() in [i.upper() for i in betuk]:
        print("Ezt a betut mar rogzitettem.")
    else:
        betuk.append(user_input)
    betuk.sort()
    print(", ".join(betuk))
