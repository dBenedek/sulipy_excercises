# https://sulipy.hu/eljarasok_fuggvenyek/eljaras?tab=feladatok

def mezot_rajzol(x=int, y=int):
    """ x: x koordinata, y: y koordinata"""
    for sor in range(3):
        for oszlop in range(6):
            if sor == x and oszlop == y:
                print("X ", end="")
            else:
                print("O ", end="")
        print()

while True:
    user_input = str(input("Add meg a kivant koordinatakat (vesszovel elvalasztva, space nelkul): "))
    coord = user_input.split(",")
    if int(coord[0]) < 0 or int(coord[1]) < 0:
        break
    mezot_rajzol(int(coord[0]), int(coord[1]))
