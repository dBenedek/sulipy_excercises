# https://sulipy.hu/ciklusok/while_ciklus?tab=feladatok

paros = False
while paros is False:
    input_num = int(input("Adj meg egy paros szamot: "))
    if input_num % 2 == 0 and input_num != 0:
        paros = True