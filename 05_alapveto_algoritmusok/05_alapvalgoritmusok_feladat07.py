# https://sulipy.hu/alapveto_algoritmusok/szelsoertek?tab=feladatok

szamok = list()
keep_going = True
while keep_going:
    user_input = input("Adj meg egy egesz szamot (kilepes: x): ")
    if user_input == "x" or user_input == "X":
        keep_going = False
    else:
        szamok.append(int(user_input))

print(f"A legnagyobb szam: {max(szamok)}")
print(f"A legkisebb szam: {min(szamok)}")