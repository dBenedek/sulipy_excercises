# https://sulipy.hu/alapveto_algoritmusok/kereses?tab=feladatok

user_input = str(input("Adj meg egy szoveget: ")).lower()

maganhangzok = ["a", "e", "i", "o", "u"]

for betu in maganhangzok:
    if betu in user_input:
        print(f"A megadott szovegben talalhato {betu}.")
        print(f"Az {betu} betu {user_input.count(betu)}-szer szerepel a szovegben.")
        betu_poziciok = ", ".join([str(idx+1) for idx in range(len(user_input)) if user_input[idx] == betu])
        print(f"Az {betu} az alabbi poziciokban fordul elo a megadott szovegben: {betu_poziciok}")
        print("-"*80)
    else:
        print(f"{betu} nem talalhato a megadott szovegben.")
        print("-" * 80)