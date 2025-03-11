# https://sulipy.hu/eljarasok_fuggvenyek/fuggveny?tab=feladatok

def kerulet(x, *args):
    if len(args) == 0:
        print("Ez egy negyzet.")
        k = x*4
    elif len(args) == 1:
        print("Ez egy teglalap.")
        k = x*2 + args[0]*2
    elif len(args) == 2:
        print("Ez egy haromszog.")
        k = x + args[0] + args[1]
    else:
        print("Ez egy sokszog.")
        k = x
        for a in args:
            k += a
    return k

print(kerulet(1, 2, 3, 4))
print(kerulet(3))
print(kerulet(2, 5))
print(kerulet(3, 2, 5))