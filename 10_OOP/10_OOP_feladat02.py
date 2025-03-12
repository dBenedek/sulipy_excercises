# https://sulipy.hu/oop/osztaly_objektum?tab=feladatok

import random

class KutyaAdat:
    def __init__(self, nev:str, eletkor:int, nem:str):
        self.nev = nev
        self.eletkor = eletkor
        self.nem = nem
    def adatokat_kiir(self):
        print(f"{self.nev} kutya {self.eletkor} eves, neme pedig: {self.nem}")

kutyak = list()
while True:
    user_input = input("Add meg a kutya nevet (kilepes: ENTER): ")
    if user_input == "":
        break
    else:
        kutya = KutyaAdat(user_input, random.randrange(0, 21), random.choice(["him", "nosteny"]))
        kutyak.append(kutya)

for k in kutyak:
    k.adatokat_kiir()
