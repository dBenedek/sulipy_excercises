# https://sulipy.hu/adattipusok/listakat_tartalmazo_listak?tab=feladatok

tarolo = [["O " for x in range(3)] for y in range(3)]

def print_racs(nested_list=list, X_helye=list):
    """ Kiirja a megadott 3x3-as listat, X-et teve a megadott helyre.
        Megvaltoztatja  a kulso 'tarolo' listat."""
    print("")
    for y in range(len(nested_list)):
        for x in range(len(nested_list[y])):
            if x == X_helye[0] and y == X_helye[1]:
                print("X ", end="")
                tarolo[y][x] = "X "
            else:
                print(nested_list[y][x], end="")
        print("")
    print("")

def koord_bekeres():
    """ Bekeri a felhasznalatol az X, Y koordinatakat, es listakent visszaadja."""
    user_input = str(input("Adj meg egy koordinatat (vesszovel elvalasztva, szokoz nelkul)! "))
    return list(map(lambda szam: int(szam), user_input.split(",")))

def main():
    while True:
        user_koord = koord_bekeres()
        # Ha X, Y a megadhato koordinatakon kivul van:
        if (user_koord[0] > 2) and (user_koord[1] > 2):
            print("Tartomanyon kivul megadott koordinata!")
            break
        else:
            print_racs(tarolo, user_koord)

main()

