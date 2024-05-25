# -*- coding: utf-8 -*-
"""
@author: Laguda Carlo
"""
from esterno import Utente
from sportivo import Sportivo

def stampa_msg_benvenuto():
    print("Ciao a tutti")
    print("Autore: Carlo Laguda")
    print("Versione: 1.1.3")
    print("Data di rilascio: 17/01/2024")


stampa_msg_benvenuto()

utente1 = Utente()
utente1.chiedi_nome()
utente1.chiedi_cognome()
utente1.chiedi_citta()
utente1.chiedi_altezza()
utente1.chiedi_peso()
utente1.chiedi_data()

i = 0
ripeti = True
while ripeti:
    ripeti = False;
    risposta = input("Sei uno tifoso? (si) o (no): ")
    if "si" in risposta:
        sportivo1 = Sportivo(utente1)
        sportivo1.chiedi_squadra()
        sportivo1.chiedi_anni_tifo_squadra()
        numeri_schede = int(input("Inserisci il numero di schede da stampare: "))
        for i in range(numeri_schede):
            sportivo1.stampa_scheda_utente()
    elif "no" in risposta:
        numeri_schede = int(input("Inserisci il numero di schede"))
        for i in range(numeri_schede):
            utente1.stampa_scheda_utente()
    else:
        print("Sei stato poco chiaro, reinserici la risposta")
        ripeti = True
