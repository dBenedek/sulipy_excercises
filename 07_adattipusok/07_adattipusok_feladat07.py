# https://sulipy.hu/adattipusok/szotar?tab=feladatok

import random
import pprint

vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "	Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]

def diak_adat_generalas():
    adatok = {"nev":random.choice(vezeteknevek) + " " + random.choice(keresztnevek),
                "eletkor":random.randrange(14, 20),
               "evfolyam":random.randrange(9, 13),
               "osztaly":random.choice(["A", "B", "C"]),
               "cim":{"telepules":random.choice(telepulesek),
                      "utca":random.choice(utcak),
                      "hazszam":random.randrange(1, 51)}}
    return adatok

diak_adatok = [diak_adat_generalas() for x in range(8)]

pprint.pprint(diak_adatok)