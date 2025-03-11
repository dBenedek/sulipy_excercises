# https://sulipy.hu/eljarasok_fuggvenyek/referenciak?tab=feladatok

def lista_modosit(x=list):
    user_input = str(input("Adj meg harom betut egyben irva: "))
    for i in range(len(x)):
        x[i] = user_input[i]

def main():
    lista = ["a", "b", "c"]
    print(lista)
    while lista.count(lista[0]) != 3:
        lista_modosit(lista)
        print(lista)

main()