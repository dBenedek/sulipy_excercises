# https://sulipy.hu/fajlkezeles/beolvasas?tab=feladatok

file = open("../data/Rilke_A_parduc.txt")

file_data = file.read()

szavak_szama = len(file_data.strip().replace("\n", " ").split(" "))
betuk_szama = len([i for i in file_data if i not in ["\n", ".", ",", " ", ":", "-"]])
maganhangzok_szama = len([i for i in [i for i in file_data if i not in ["\n", ".", ",", " ", ":", "-"]] if i.lower() in ["a", "e", "i", "u", "o", 'ü', 'ö', 'ű', 'á', 'é']])

print(f"Szavak szama: {szavak_szama}")
print(f"Maganhangzok szama: {maganhangzok_szama}")
print(f"Betuk szama: {betuk_szama}")

file.close()