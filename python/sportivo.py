# -*- coding: utf-8 -*-
"""
@author: Laguda Carlo
"""
from esterno import Utente
import datetime
class Sportivo(Utente):
    def __init__(self, utente1):
        self.nome = utente1.nome
        self.cognome = utente1.cognome
        self.cittaNascita = utente1.cittaNascita
        self.dataNascitaUtente = utente1.dataNascitaUtente
        self.altezzaUtente = utente1.altezzaUtente
        self.pesoUtente = utente1.pesoUtente
        self.eta = 0
        self.squadra = "Milan"
        self.anniTifoSquadra = 10
        

    def chiedi_squadra(self):
        ripeti = True
        while ripeti:
            self.squadra = input("Inserisci la tua squadra preferita: ")
            nome = input("Inserisci il tuo nome: ").strip()
            if squadra.isalnum()():
                self.squadra = squadra
                break
            else:
                print("Errore: il nome deve contenere solo lettere.")
       

    def chiedi_anni_tifo_squadra(self):
        oggi = datetime.today()
        data_nascita = datetime.strptime(self.dataNascitaUtente, "%d/%m/%Y")
        self.eta = oggi.year - data_nascita.year 
        ripeti = True
        while ripeti:
            try:
                anniTifoSquadra = int(input("Da quanti anni tifi questa squadra: "))
                if 0 < anniTifoSquadra < self.eta - 2:
                    self.anniTifoSquadra = anniTifoSquadra
                    break
                else:
                    print("Hai inserito un dato errato, devi tifare la tua squadra da almeno 1 anno. Riprova:")
            except ValueError:
                print("Hai inserito un dato errato, deve essere un numero intero.")

    def stampa_scheda_utente(self):
        print("-------------------------------------------")
        print("Il tuo nome:", self.nome.upper())
        print("Il tuo cognome:", self.cognome.upper())
        print("La città dove vivi:", self.cittaNascita.upper())
        print("Il tuo peso in Kg:", self.pesoUtente)
        print("La tua altezza in metri:", self.altezzaUtente)
        print("La tua data di nascita:", self.dataNascitaUtente)
        print("La squadra che tifi:", self.squadra.upper())
        print("Da quanti anni tifi la tua squadra:", self.anniTifoSquadra)
        print("-------------------------------------------")
