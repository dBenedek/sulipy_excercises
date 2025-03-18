# https://sulipy.hu/oop/alapelvei?tab=feladatok

class Diak:
    def __init__(self, nev:str, osztaly:str):
        self.nev = nev
        self.osztaly = osztaly
    def diak_kiir(self):
        print(f"Szia, a nevem {self.nev}, es a(z) {self.osztaly} osztalyba jarok.")

class Tanar(Diak):
    def __init__(self, nev:str, osztaly:str, szak:str):
        super().__init__(nev, osztaly)
        self.szak = szak
    def tanar_kiir(self):
        print(f"Szia, a nevem {self.nev}, es {self.szak} szakos tanar vagyok.")

diak_01 = Diak("Kovacs Jakab", "1.A")
diak_02 = Diak("Maros Helga", "11.B")
tanar_01 = Tanar("Dr. Bagdi Eszmeralda", "-", "biologia-kemia")
tanar_02 = Tanar("Kovacs Kazuar", "-", "hittan")

diak_01.diak_kiir()
diak_02.diak_kiir()
tanar_01.tanar_kiir()
tanar_02.tanar_kiir()