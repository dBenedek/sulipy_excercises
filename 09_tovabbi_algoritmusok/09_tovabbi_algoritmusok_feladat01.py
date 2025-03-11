# https://sulipy.hu/tovabbi_algoritmusok/lekepezes?tab=feladatok

def atalakit_rendszam(rendszam:str):
    r = list(rendszam)
    for idx, v in enumerate(r):
        if v in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            r[idx] = "*"
        else:
            r[idx] = "|"
    return "".join(r)

rendszamok = ['ABC123', 'ABCD777', 'WN25L']
atalakitott_rendszamok = list(map(atalakit_rendszam, rendszamok))

print(f"{atalakitott_rendszamok=}")

