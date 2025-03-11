# https://sulipy.hu/tovabbi_algoritmusok/rendezes?tab=feladatok

import random

interv = input("Adj meg egy intervallumot (vesszovel elvalasztva, space nelkul): ")
szamok = int(input("Add meg, hogy hany szamot szeretnel: "))

interv_s = int(interv.split(",")[0])
interv_e = int(interv.split(",")[1])
rand_szamok = [random.randrange(interv_s, interv_e+1, 1) for i in range(szamok)]

print(sorted(rand_szamok))
print(sorted(rand_szamok, reverse=True))