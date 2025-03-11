# https://sulipy.hu/adattipusok/listakat_tartalmazo_listak?tab=feladatok

import random

lista = [[random.randrange(-5, 6) for i in range(3)] for x in range(5)]

print("Veletlenszamok:")
print(lista)

lista_nem_negativ = [[i for i in j if i > 0] for j in lista]

print("Nemnegativ veletlenszamok:")
print(lista_nem_negativ)