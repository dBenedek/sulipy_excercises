# https://sulipy.hu/fajlkezeles/kiiras?tab=feladatok

with open("/home/benedek_danko/PycharmProjects/sulipy_excercises/data/Timeline_of_ programming_languages.txt", "r") as forrasfile:
    with open("/home/benedek_danko/PycharmProjects/sulipy_excercises/data/Timeline_of_ programming_languages_copy.txt", "w") as celfile:
        nyelvek = list()
        for sor in forrasfile:
            s = sor.strip().split(";")
            if (len(s) > 1) and (s[1] not in nyelvek):
                nyelvek.append(s[1])
                celfile.write(s[1] + " " + s[0] + "\n")

forrasfile.close()
celfile.close()