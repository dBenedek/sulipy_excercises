# https://sulipy.hu/oop/kapcsolatok?tab=feladatok

class Varos:
    """ Varos class object."""
    def __init__(self, pop2023, pop2022, city, country, continent, growth_rate, rank):
        self.pop2023 = pop2023
        self.pop2022 = pop2022
        self.city = city
        self.country = country
        self.continent = continent
        self.growth_rate = growth_rate
        self.rank = rank

class VarosLista:
    """ Operations with a list of the Varos objects."""
    def __init__(self, path):
        self.path = path
        self.varosok_lista = []
    def adatot_beolvas(self):
        """ Read and store the data of cities."""
        with open(self.path, "r") as file:
            for sor in file:
                sor_lista = sor.strip().split(",")
                self.varosok_lista.append(Varos(sor_lista[0], sor_lista[1],
                                                sor_lista[2], sor_lista[3],
                                                sor_lista[4], sor_lista[5],
                                                sor_lista[6]))
        file.close()
    def varost_kiir(self):
        """ Print the details of each city."""
        for varos in self.varosok_lista[1:]:
            print(f"\nVaros: {varos.city}, orszag: {varos.country}, kontinens: {varos.continent}.")
            print(f"Lakossaga 2022-ben {varos.pop2022} fo, 2023-ban {varos.pop2023} fo.")
            print(f"Ez egy {varos.growth_rate} novekedesi ratat jelent, illetve a vilagon a(z) {varos.rank}-ik.")
    def varos_leker(self, valasztott_varos):
        """ Print the details of a selected city."""
        if valasztott_varos.lower() in list(v.city.lower() for v in self.varosok_lista):
            for index, item in enumerate(self.varosok_lista):
                if item == valasztott_varos:
                    break
                else:
                    continue
            print("A megadott varos szerepel a valaszthato varosok kozott. Adatai:")
            print(f"Orszag: {self.varosok_lista[index].country}, kontinens: {self.varosok_lista[index].continent}")
            print(f"Lakossag (2022): {int(self.varosok_lista[index].pop2022):,d} fo")
            print(f"Lakossag (2023): {int(self.varosok_lista[index].pop2023):,d} fo")
            print(f"Novekedesi rata: {self.varosok_lista[index].growth_rate}")
            print(f"Rangsorban helyezes: {self.varosok_lista[index].rank}.")
        else:
            print("A megadott varos nem szerepel a valaszthato varosok listajaban.")

def main():
    # Create object:
    varosok_top = VarosLista("/home/benedek_danko/PycharmProjects/sulipy_excercises/data/pop2023.csv")
    # Read and store data:
    varosok_top.adatot_beolvas()
    # Print each Varos object:
    varosok_top.varost_kiir()
    # Print the details of a selected city by user:
    while True:
        valasztott_varos = input("\nAdj meg egy varost az adatai lekeresehez (kielepes: ENTER): ")
        if valasztott_varos == "":
            break
        else:
            varosok_top.varos_leker(valasztott_varos=valasztott_varos)

# Call the main function:
main()