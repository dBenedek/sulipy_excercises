# https://sulipy.hu/fajlkezeles/beolvasas?tab=feladatok

adatok = []
with open("../data/Timeline_of_programming_languages.txt", "r") as file:
    for sor in file:
        adat = sor.strip().split(";")
        if len(adat) == 4:
            adatok.append({"year":adat[0], "programming language":adat[1],
                          "first name":adat[2], "last name":adat[3]})

del adatok[0]
print(adatok)
