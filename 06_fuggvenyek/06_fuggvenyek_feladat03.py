# https://sulipy.hu/eljarasok_fuggvenyek/fuggveny?tab=feladatok

def legkisebb(szamok=list):
    print(f"Legkisebb szam: {str(min(szamok))}")
    return min(szamok)

szamok = list()
while True:
    user_input = int(input("Adj meg egy egesz szamot (kilepes: negativ szam): "))
    if user_input < 0:
        if len(szamok) != 0:
            legkisebb(szamok)
        else:
            print("A lista ures.")
        break
    elif user_input > 0:
        szamok.append(user_input)
    else:
        continue


