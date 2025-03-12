# https://sulipy.hu/oop/osztaly_objektum?tab=feladatok

class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz
    def kerulet_szamitas(self):
        return self.oldal_hossz*4
    def terulet_szamitas(self):
        return self.oldal_hossz**2
    def info(self):
        print(f"A {self.oldal_hossz} oldalhosszusagu negyzet kerulete {self.kerulet_szamitas():.2f}, teruletel pedig {self.terulet_szamitas():.2f}.")

negyzetek = list()
while True:
    user_input = input("Add meg e negyzet oldalhosszusagat (kilepes: 0): ")
    if user_input == "0":
        break
    else:
        negyzetek.append(Negyzet(int(user_input)))

for n in negyzetek:
    n.info()
