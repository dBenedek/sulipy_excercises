# https://sulipy.hu/oop/osztalyok_jellemzoi?tab=feladatok

import datetime
import random

class Diak:
    a_osztalyosok_szama = 0
    b_osztalyosok_szama = 0
    def __init__(self, nev:str, osztaly:str, szuletesi_ev:int):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
        if self.osztaly[-1].upper() == "A":
            type(self).a_osztalyosok_szama += 1
        else:
            type(self).b_osztalyosok_szama += 1
    def eletkor(self):
        return datetime.datetime.now().year - self.szuletesi_ev
    def info(self):
        print(f"Szia, {self.nev} vagyok, a {self.osztaly} osztalyba jarok, {self.eletkor()} eves vagyok.")
    @classmethod
    def osztalyok_osszesit(cls):
        return cls.a_osztalyosok_szama, cls.b_osztalyosok_szama
    @staticmethod
    def infot_kiir():
        return "\nAz XY iskola koszonti az erdeklodoket."

vezetek_nevek = ["Lakatos", "Kovacs", "Brunyevszky", "Nagy", "Molnar", "Fekete"]
kereszt_nevek = ["Abel", "Anna", "Janos", "Maria", "Valentin", "Karola"]
osztalyok = [str(i) for i in range(1, 13)]
osztalyok_ab = ["A", "B"]

tanulok = [Diak(nev = random.choice(vezetek_nevek) + " " + random.choice(kereszt_nevek),
                osztaly = random.choice(osztalyok) + "." + random.choice(osztalyok_ab),
                szuletesi_ev = random.randrange(2007, 2020)) for i in range(5)]

a_osztalyosok_szama, b_osztalyosok_szama = Diak.osztalyok_osszesit()
print(Diak.infot_kiir())
print(f"A osztalyos tanulok szama: {a_osztalyosok_szama}, B osztalyos tanulok szama: {b_osztalyosok_szama}\n")

for d in tanulok:
    d.info()
