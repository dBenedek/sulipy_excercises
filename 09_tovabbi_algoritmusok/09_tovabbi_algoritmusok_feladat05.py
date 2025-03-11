# https://sulipy.hu/tovabbi_algoritmusok/unio_metszet?tab=feladatok

import random

lista_01 = list(random.randrange(-5, 6) for i in range(5))
lista_02 = list(random.randrange(-5, 6) for i in range(5))

# A ket lista:
print(lista_01, lista_02)
# Metszet:
print(set(lista_01) & set(lista_02))
# Unio:
print(set(lista_01) | set(lista_02))