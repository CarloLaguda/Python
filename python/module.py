# Definiamo una funzione di saluto che accetta un nome come parametro e restituisce un saluto personalizzato
def greet(name):
    return f"Hello, {name}!"

# Definiamo una funzione per aggiungere due numeri
def add(a, b):
    return a + b

# Dichiarazione di una variabile globale PI
PI = 3.14159

# Definiamo una classe Studente con alcuni attributi e metodi
class Studente:
    # Metodo di inizializzazione con nome ed età dello studente
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        self.numeroStampe = 0
        self.annoNascita = 0

    # Metodo per chiedere all'utente di inserire il proprio nome
    def chiediNome(self):
        self.nome = input("Inserisci il tuo nome:")
        
    # Metodo per chiedere all'utente di inserire la propria età con validazione
    def chiediEta(self):
        ripeti = True
        while ripeti:
            try:       
                self.eta = int(input("Inserisci la tua età:")) 
                if 0 < self.eta < 120:
                    ripeti = False
                    print("Il dato inserito", str(self.eta), "è valido.")
                else:
                    ripeti = True
                    print("Il dato inserito è errato, deve essere un numero intero maggiore di 0 e minore di 120.")
            except:
                ripeti = True
                print("Il dato inserito è assurdo, riprova.")

    # Metodo per chiedere all'utente di inserire il proprio anno di nascita con validazione
    def chiediAnnoNascita(self):
        ripeti = True
        while ripeti:
            try:       
                self.annoNascita = int(input("Inserisci il tuo anno di nascita:")) 
                if 1900 < self.annoNascita < 2024:
                    ripeti = False
                    print("Il dato inserito", str(self.annoNascita), "è valido.")
                else:
                    ripeti = True
                    print("Il dato inserito è errato, deve essere un numero intero maggiore di 1900 e minore di 2024.")
            except:
                ripeti = True
                print("Il dato inserito è assurdo, riprova.")

    # Metodo per stampare le schede finali dello studente
    def stampaSchede(self):
        for x in range(self.numeroStampe):
            print("*********************************")
            print("* Nome:", self.nome.upper())
            print("* Età:", self.eta)
            print("*********************************")

    # Metodo per chiedere all'utente il numero di schede finali da stampare con validazione
    def chiediNumeroStampe(self):
        ripeti = True
        while ripeti:
            try:       
                self.numeroStampe = int(input("Inserisci il numero di schede finali da stampare:")) 
                if 0 < self.numeroStampe < 10:
                    ripeti = False
                    print("Il dato inserito", str(self.numeroStampe), "è valido.")
                else:
                    ripeti = True
                    print("Il dato inserito è errato, deve essere un numero intero maggiore di 0 e minore di 10.")
            except:
                ripeti = True
                print("Il dato inserito è assurdo, riprova.")
        else:
            # Se il ciclo while termina senza eccezioni, chiamiamo il metodo per stampare le schede
            self.stampaSchede()
