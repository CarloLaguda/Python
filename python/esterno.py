# -*- coding: utf-8 -*-
"""
@author: Laguda Carlo
"""
class Utente:
    def __init__(self):
        self.nome = "Pio"
        self.cognome = "Rossi"
        self.cittaNascita = "Milano"
        self.giornoNascitaUtente = 7
        self.meseNascitaUtente = 3
        self.annoNascitaUtente = 2005
        self.pesoUtente = 80
        self.altezzaUtente = 1.76
        self.dataNascitaUtente = ""

    def chiedi_nome(self):
        ripeti = True
        while ripeti:
            nome = input("Inserisci il tuo nome: ").strip()
            if nome.isalpha():
                self.nome = nome
                break
            else:
                print("Errore: il nome deve contenere solo lettere.")

    def chiedi_cognome(self):
        ripeti = True
        while ripeti:
            cognome = input("Inserisci il tuo cognome: ").strip()
            if cognome.isalpha():
                self.cognome = cognome
                break
            else:
                print("Errore: il cognome deve contenere solo lettere.")

    def chiedi_citta(self):
        ripeti = True
        while ripeti:
            cittaNascita = input("Inserisci la tua città di nascita: ").strip()
            if cittaNascita.isalpha():
                self.cittaNascita = cittaNascita
                break
            else:
                print("Errore: la città di nascita deve contenere solo lettere.")

    def chiedi_altezza(self):
        ripeti = True
        while ripeti:
            try:
                altezzaUtente = float(input("Inserisci la tua altezza in metri: "))
                if 0.4 <= altezzaUtente <= 2.5:
                    self.altezzaUtente = altezzaUtente
                    break
                else:
                    print("Errore: l'altezza deve essere compresa tra 0.4 e 2.5 metri.")
            except ValueError:
                print("Errore: inserisci un valore numerico valido.")

    def chiedi_data(self):
         ripeti = True
         ciclotot = True
         while ciclotot:
             while ripeti:
                 try:
                     self.giornoNascitaUtente = int(input("Inserisci il tuo giorno di nascita: "))
                     if 0 < self.giornoNascitaUtente < 32:
                         break
                     else:
                         print("Hai inserito un dato errato, il giorno di nascita deve essere maggiore di 0 e minore di 32")
                 except ValueError:
                     print("Hai inserito un dato errato, deve essere un numero intero.")

             while ripeti:
                 try:
                     self.meseNascitaUtente = int(input("Inserisci il tuo mese di nascita: "))
                     if 0 < self.meseNascitaUtente < 13:
                         break
                     else:
                         print("Hai inserito un dato errato, il mese di nascita deve essere compreso tra 1 e 12")
                 except ValueError:
                     print("Hai inserito un dato errato, deve essere un numero intero.")

             while ripeti:
                 try:
                     self.annoNascitaUtente = int(input("Inserisci il tuo anno di nascita: "))
                     if 1920 < self.annoNascitaUtente < 2025:
                         break
                     else:
                         print("Hai inserito un dato errato, l'anno di nascita deve essere compreso tra 1920 e 2024")
                 except ValueError:
                     print("Hai inserito un dato errato, deve essere un numero intero.")

             max_giorno_mese = 0
             if self.meseNascitaUtente in [1, 3, 5, 7, 8, 10, 12]:
                 max_giorno_mese = 31
             elif self.meseNascitaUtente in [4, 6, 9, 11]:
                 max_giorno_mese = 30
             else:
                 if self.annoNascitaUtente % 4 == 0:
                     max_giorno_mese = 29
                 else:
                     max_giorno_mese = 28

             if self.giornoNascitaUtente <= max_giorno_mese:
                 self.dataNascitaUtente = f"{self.giornoNascitaUtente}/{self.meseNascitaUtente}/{self.annoNascitaUtente}"
                 ciclotot = False
             else:
                 print("Data di nascita non valida, reinseriscila")
                 ciclotot = True

             
                 
    def chiedi_peso(self):
        ripeti = True
        while ripeti:
            try:
                self.pesoUtente = float(input("Inserisci il tuo peso in KG usando la virgola come separatore: "))
                if 15 < self.pesoUtente < 180:
                    break
                else:
                    print("Hai inserito un dato errato, il peso deve essere compreso tra 15 e 180.")
            except ValueError:
                print("Hai inserito un dato errato, il peso deve essere un numero.")

    
    def stampa_scheda_utente(self):
        print("*******************************************")
        print("Il tuo nome:", self.nome.upper())
        print("Il tuo cognome:", self.cognome.upper())
        print("La città dove vivi:", self.cittaNascita.upper())
        print("Il tuo peso in Kg:", self.pesoUtente)
        print("La tua altezza in metri:", self.altezzaUtente)
        print("La tua data di nascita:", self.dataNascitaUtente)
        print("*******************************************")

