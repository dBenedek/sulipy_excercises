# https://sulipy.hu/ciklusok/while_ciklus?tab=feladatok

input_str = str(input("Adj meg egy szoveget: "))
input_num = abs(int(input("Hanyszor irjam ezt ki?")))

while input_num != 0:
    print(input_str)
    input_num -= 1