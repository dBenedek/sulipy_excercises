# https://sulipy.hu/alapveto_algoritmusok/osszegzes?tab=feladatok

keep_going = True
szamok = list()
while keep_going:
    user_input = int(input("Adj meg egesz szamot [-5;5] intervallumban: "))
    if (user_input < -5) or (user_input > 5):
        keep_going = False
    else:
        szamok.append(user_input)

print(szamok)
print(sum([i for i in szamok if i % 2 == 0]))