# https://sulipy.hu/tovabbi_algoritmusok/rendezes?tab=feladatok

def arat_visszaad(butorok:list):
    return sorted(butorok, key=lambda x: int(x["ar"]))

butorok = list()
with open("/home/benedek_danko/PycharmProjects/sulipy_excercises/data/butorok.txt", "r") as file:
    for sor in file:
        sor = sor.strip().split(";")
        butor = {"tipus":sor[0],
                 "butor":sor[1],
                 "osztaly":sor[2],
                 "ar":sor[3],
                 "raktaron":True if sor[4] == "igen" else False}
        butorok.append(butor)

file.close()
del butorok[0]

print(arat_visszaad(butorok))