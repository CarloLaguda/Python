import datetime

class AutoUsate:
    def __init__(self):
        self.nome = []
        self.cognome = []
        self.modello = ""
        self.marca = ""
        self.anno_immatricolazione = 0
        self.prezzo_vendita = 0.0

    def chiedi_nome(self):
        while True:
            nome_inserito = input("Inserisci il tuo nome (massimo 3 nomi): ").strip().upper()
            if nome_inserito.replace(' ', '').isalpha():  # Controllo anche per spazi
                nome = nome_inserito.split()
                if len(nome) <= 3:
                    self.nome = nome
                    break
                else:
                    print("Puoi inserire massimo 3 nomi contenenti solo lettere.")
            else:
                print("Il nome deve contenere solo caratteri alfabetici")

    def chiedi_cognome(self):
        while True:
            cognome = input("Inserisci il tuo cognome (massimo 3 cognomi): ").strip().upper()
            if cognome.replace(' ', '').isalpha():  # Controllo anche per spazi
                cognomi = cognome.split()
                if len(cognomi) <= 3:
                    self.cognome = cognomi
                    break
                else:
                    print("Puoi inserire massimo 3 cognomi contenenti solo lettere.")
            else:
                print("Il cognome deve contenere solo caratteri alfabetici")

    def chiedi_modello(self):
        self.modello = input("Inserisci il modello dell'auto da vendere: ").strip().upper()

    def chiedi_marca(self):
        self.marca = input("Inserisci la marca dell'auto da vendere: ").strip().upper()

    def chiedi_anno_immatricolazione(self):
        anno_Corrente = datetime.datetime.now().year
        while True:
            try:
                anno_immatricolazione = int(input("Inserisci l'anno di immatricolazione dell'auto: "))
                if 1960 <= anno_immatricolazione <= anno_Corrente:
                    self.anno_immatricolazione = anno_immatricolazione
                    break
                else:
                    print("Il dato inserito è errato, deve essere un numero intero maggiore di 1960 e minore o uguale a " + str(anno_Corrente) + ".")
            except ValueError:
                print("Il dato inserito è assurdo, riprova.")

    def chiedi_prezzo_vendita(self):
        while True:
            try:
                prezzo_vendita = float(input("Inserisci il prezzo di vendita dell'auto usata: "))
                if prezzo_vendita > 0:
                    self.prezzo_vendita = prezzo_vendita
                    break
                else:
                    print("Il prezzo di vendita deve essere un numero positivo.")
            except ValueError:
                print("Il dato inserito è assurdo, riprova.")

    def stampa_schede(self):
        while True:
            try:
                n_schede = int(input("Inserisci il numero di schede che vuoi stampare: "))
                if n_schede > 0:
                    for _ in range(n_schede):
                        print("*********************************")
                        print("Nome: " + " ".join(self.nome))
                        print("Cognome: " + " ".join(self.cognome))
                        print("Modello dell'auto: " + self.modello)
                        print("Marca dell'auto: " + self.marca)
                        print("Anno di immatricolazione: " + str(self.anno_immatricolazione))
                        print("Prezzo di vendita: " + str(self.prezzo_vendita))
                        print("*********************************")
                    break
                else:
                    print("Il numero di schede deve essere maggiore di zero.")
            except ValueError:
                print("Il numero di schede deve essere un numero intero positivo.")

