# https://sulipy.hu/tovabbi_algoritmusok/valogatas?tab=feladatok

raktaron = list()
nincs_raktaron = list()
with open("/home/benedek_danko/PycharmProjects/sulipy_excercises/data/butorok.txt", "r") as file:
    for sor in file:
        sor = sor.strip().split(";")
        butor = {"tipus":sor[0],
                 "butor":sor[1],
                 "osztaly":sor[2],
                 "ar":sor[3],
                 "raktaron":True if sor[4] == "igen" else False}
        if butor["raktaron"]:
            raktaron.append(butor)
        else:
            nincs_raktaron.append(butor)

file.close()
del nincs_raktaron[0]

print(raktaron)
print(nincs_raktaron)