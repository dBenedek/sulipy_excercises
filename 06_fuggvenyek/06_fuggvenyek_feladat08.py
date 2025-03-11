# https://sulipy.hu/eljarasok_fuggvenyek/lambda?tab=feladatok

szavak = ["alma", "narcisz", "granat", "ujsag", "kalapacs"]

print(sorted(szavak, key=lambda szo: szo[1]))

azonositok = ['id10', 'id100', 'id23', 'id2', 'id13', 'id1']

print(sorted(azonositok, key=lambda azonosito: int(azonosito[2:])))

szavak = ['alma', 'ló', 'padló', 'citrom', 'kávé', 'nyugalom']

print(list(filter(lambda szo: "l" not in szo, szavak)))

print([szo for szo in szavak if "l" not in szo])