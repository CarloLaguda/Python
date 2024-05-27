# studente_Laguda.py
# @author: Laguda Carlo
# Classe: 3F
# Data: 27/05/2024
# Versione: 1.0.2

import datetime

class Studente:
    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.eta = 0
        self.istituto = ""
        self.classe = ""
        self.anno_iscrizione = 0

    def chiedi_nome(self):
        while True:
            nome = input("Inserisci il tuo nome (massimo 3 nomi): ").strip().upper()
            nomi = nome.split()
            if len(nomi) <= 3:
                self.nome = nome
                break
            else:
                print("Puoi inserire massimo 3 nomi.")

    def chiedi_cognome(self):
        while True:
            cognome = input("Inserisci il tuo cognome (massimo 3 cognomi): ").strip().upper()
            cognomi = cognome.split()
            if len(cognomi) <= 3:
                self.cognome = cognome
                break
            else:
                print("Puoi inserire massimo 3 cognomi.")

    def chiedi_nomeIstituto(self):
        while True:
            istituto = input("Inserisci il nome del tuo istituto: ").strip().upper()
            if istituto.replace(" ", "").isalpha():
                self.istituto = istituto
                break
            else:
                print("Il nome dell'istituto deve contenere solo lettere e spazi.")

    def chiedi_classe(self):
        self.classe = input("Inserisci la tua classe: ").strip().upper()

    def chiedi_Eta(self):
        while True:
            try:
                eta = int(input("Inserisci la tua età: "))
                if 1 < eta < 120:
                    self.eta = eta
                    break
                else:
                    print("Il dato inserito è errato, deve essere un numero intero maggiore di 0 e minore di 120.")
            except ValueError:
                print("Il dato inserito è assurdo, riprova.")

    def chiedi_AnnoIscrizione(self):
        current_year = datetime.datetime.now().year
        while True:
            try:
                anno_iscrizione = int(input("Inserisci l'anno in cui ti sei iscritto: "))
                if 2000 < anno_iscrizione <= current_year:
                    self.anno_iscrizione = anno_iscrizione
                    break
                else:
                    print("Il dato inserito è errato, deve essere un numero intero maggiore di 2000 e minore o uguale a " + str(current_year) + ".")
            except ValueError:
                print("Il dato inserito è assurdo, riprova.")

    def stampa_scheda_utente(self):
        while True:
            try:
                n_schede = int(input("Inserisci il numero di schede che vuoi stampare: "))
                if n_schede < 1:
                    raise ValueError
                for _ in range(n_schede):
                    print("*********************************")
                    print("Nome: " + self.nome)
                    print("Cognome: " + self.cognome)
                    print("La tua età: " + str(self.eta))
                    print("Nome dell'istituto: " + self.istituto)
                    print("Classe: " + self.classe)
                    print("Anno di iscrizione: " + str(self.anno_iscrizione))
                    print("*********************************")
                break
            except ValueError:
                print("Il numero di schede deve essere un numero intero positivo.")
