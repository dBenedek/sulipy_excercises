# https://sulipy.hu/adattipusok/tuple?tab=feladatok

def koord_beker():
    pont1_koord = input("Add meg az elso pont X,Y koordinatait (vesszovel elvalasztva, space nelkul): ")
    pont2_koord = input("Add meg a masodik pont X,Y koordinatait (vesszovel elvalasztva, space nelkul): ")
    if pont1_koord == "" or pont2_koord == "":
        return False
    pont1_koord_tuple = tuple(list(int(i) for i in pont1_koord.split(",")))
    pont2_koord_tuple = tuple(list(int(i) for i in pont2_koord.split(",")))
    return pont1_koord_tuple, pont2_koord_tuple

def tavolsag_szamitas(koord_1:tuple, koord_2:tuple):
    return round(((koord_1[0] - koord_2[0])**2 + (koord_1[1] - koord_2[1])**2)**.5, 3)

def kozelebb_origohoz(koord_1:tuple, koord_2:tuple):
    koord1_tav = ((koord_1[0])**2 + (koord_1[1])**2)**.5
    koord2_tav = ((koord_2[0]) ** 2 + (koord_2[1]) ** 2)**.5
    if koord1_tav > koord2_tav:
        return koord_2
    elif koord1_tav < koord2_tav:
        return koord_1
    else:
        return koord_1, koord_2

def main():
    while True:
        print("-"*40)
        koordinatak = koord_beker()
        print("-" * 40)
        if koordinatak is False:
            break
        koordinatak_tavolsag = tavolsag_szamitas(koordinatak[0], koordinatak[1])
        origo_kozelseg = kozelebb_origohoz(koordinatak[0], koordinatak[1])
        print(f"A ket pont kozotti tavolsag: {koordinatak_tavolsag}")
        print(origo_kozelseg)
        print(f"Az origohoz kozelebbi pont: {origo_kozelseg}")

main()