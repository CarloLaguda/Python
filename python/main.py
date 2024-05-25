"""Programma fortissimo di Carlo Laguda GG"""

# Stampiamo "Hello, World!"
print("Hello, World!")

# Dichiarazioni di variabili e stampa di messaggi
messaggio1 = "Buongiorno classe"
messaggio2 = "arrivederci"
print(messaggio1, messaggio2)

print("\n")#Riga vuota

# Dichiarazione di una variabile e stampa
x = "pippo"
print(x)

# Definizione di una funzione per modificare la variabile globale x
def myfunc():
    global x
    x = "fantastic"
    print(x)

# Chiamiamo la funzione e stampiamo il valore di x
myfunc()
print(x)

# Stampa il tipo di dato della variabile x dopo diverse assegnazioni
print(type(x))
x = 5
print(type(x))
x = 20.5
print(type(x))

# Liste, tuple, dizionari
x = ["apple", "banana", "cherry"]
print(type(x))

# Modifichiamo e aggiungiamo elementi alla lista
x[2] = "lampone"
x.append("arancia")
print(x)
x.pop(0)#Elimina elemento
print(x)

# Modifichiamo una tupla convertendola temporaneamente in lista per modificarla
x = ("apple", "banana", "cherry")
temp_list = list(x)
temp_list[1] = "blueberry"
x = tuple(temp_list)
print(x)  # Output: ('apple', 'blueberry', 'cherry')

# Definiamo una lista di esempio
frutti = ["mela", "banana", "ciliegia", "arancia"]

# Rimuoviamo l'elemento all'indice 1 (banana)
elemento_rimosso = frutti.pop(1)

# Visualizziamo l'elemento rimosso e la lista aggiornata
print("Elemento rimosso:", elemento_rimosso)
print("Lista aggiornata:", frutti)

# Tipi di dati non mutabili
x = ("apple", "banana", "cherry")  # Tuple
print(type(x))

# Dizionari: insiemi di chiavi e valori
x = {"name": "John", "age": 36}
print(type(x))

# Booleano: vero o falso
x = True
print(type(x))

# Esempi di operazioni sulle stringhe
x = "Hello world"
print("La precedente stringa contiene", len(x), "caratteri")
txt = "Hello world"
x = txt[0]
print("La precedente stringa contiene", x, "come primo carattere")
txt = "Hello gianni"
x = txt[2:5]
print("La precedente stringa contiene", x, "per i caratteri da indice 2 a indice 4")

# Importazione e utilizzo di un modulo chiamato 'module'
import module
greeting = module.greet("Alice")
sum_result = module.add(5, 3)
pi_value = module.PI
print(greeting)       # Output: Hello, Alice!
print(sum_result)     # Output: 8
print(pi_value)       # Output: 3.14159

from module import Studente
# Creazione di un'istanza della classe Studente dal modulo
studente1 = Studente("Gianni", 40)
print(studente1.nome)
print(studente1.eta)

# Modifica degli attributi dell'istanza studente1 e chiamata di alcuni metodi
studente1.nome = "Pippo"
studente1.eta = 50
print(studente1.nome)
print(studente1.eta)
studente1.chiediNome()
studente1.chiediAnnoNascita()
studente1.chiediEta()
studente1.chiediNumeroStampe()

# Cicli for con diversi range
for x in range(10):
    print("ciao", x)
    print("********************")
for x in range(3, 11):
    print("ciao", x)
    print("********************")
for x in range(2, 30, 2):
    print(x)

# Esempio di funzione con parametro
def my_function(fname, eta):
    eta = int(eta)
    print(fname, " hai " , eta , " anni.")

# Gestione delle eccezioni con un ciclo while
errore = True
while (errore):
    try:
        x = int(input("Inserisci la tua eta:"))
        my_function("Emil", x)
        errore = False
    except:
        print("An exception occurred")
else:
    print("Siamo usciti dal ciclo try-catch.")

# Esempio di formattazione di stringhe con il metodo format
quantita = 3
codicearticolo = 567
prezzo = 49
frase = "Voglio {0} pezzi dell'articolo numero {1} per un prezzo di {2} euro."
print(frase.format(quantita, codicearticolo, prezzo))
frase = "Voglio comprare a {2} euro l'articolo numero {1}, dammene {0} pezzi."
print(frase.format(quantita, codicearticolo, prezzo))

# Utilizzo del modulo datetime per ottenere la data corrente
import datetime
y = datetime.datetime.now()
print(y)
print(y.year)
print(y.strftime("%A"))

# Manipolazione di una stringa divisa in parole
txt = input("Inserisci il tuo nome completo:")
x = txt.split()
y = len(x)
for i in range(y):
    print("Il tuo nome n", str(i+1), "è", x[i])
print("Nel tuo nome completo ci sono ", y, "nomi.")

# Esempio di gioco indovina il numero
import random
xrnd = random.randint(1, 101)
tentativi = 0
max_tentativi = 10
while tentativi < max_tentativi:
    n_utn = int(input("Inserisci un numero compreso tra 1 e 101: "))
    tentativi += 1
    if n_utn < xrnd:
        print("Troppo basso, riprova")
    elif n_utn > xrnd:
        print("Troppo alto, riprova")
    else:
        print("Hai indovinato il numero!")
        break
if tentativi == max_tentativi and n_utn != xrnd:
    print("Hai esaurito i tentativi. Il numero era", xrnd)

# Esempio di implementazione di FizzBuzz
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
   
def verifica_pressione(eta, sistolica, diastolica):
    # Definiamo gli intervalli normali in base all'età
    if eta <= 20:
        min_sistolica, max_sistolica = 105, 135
        min_diastolica, max_diastolica = 60, 80
    elif 21 <= eta <= 30:
        min_sistolica, max_sistolica = 110, 140
        min_diastolica, max_diastolica = 65, 85
    elif 31 <= eta <= 40:
        min_sistolica, max_sistolica = 115, 145
        min_diastolica, max_diastolica = 70, 90
    elif 41 <= eta <= 50:
        min_sistolica, max_sistolica = 120, 150
        min_diastolica, max_diastolica = 75, 95
    elif 51 <= eta <= 60:
        min_sistolica, max_sistolica = 125, 155
        min_diastolica, max_diastolica = 80, 100
    else:  # eta > 60
        min_sistolica, max_sistolica = 130, 160
        min_diastolica, max_diastolica = 85, 105

    # Controlliamo se i valori della pressione rientrano nei limiti normali
    if min_sistolica <= sistolica <= max_sistolica and min_diastolica <= diastolica <= max_diastolica:
        return "I valori della pressione sono normali."
    else:
        return "I valori della pressione non sono normali."

# Input da parte dell'utente per età e valori di pressione
eta = int(input("Inserisci la tua età: "))
sistolica = int(input("Inserisci il valore della pressione sistolica: "))
diastolica = int(input("Inserisci il valore della pressione diastolica: "))

# Verifica e output del risultato
print(verifica_pressione(eta, sistolica, diastolica))


def crea_istogramma(lista):
    # Stampa un istogramma con '*' basato sui valori della lista
    for numero in lista:
        print('*' * numero)

numeri = [12, 7, 9, 5]
crea_istogramma(numeri)


def sequenza_fibonacci(n):
    # Calcola e stampa i primi n numeri della sequenza di Fibonacci
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')  # Stampa sulla stessa riga
        a, b = b, a + b
    print()

n = int(input("Quanti numeri della sequenza di Fibonacci vuoi visualizzare? "))
sequenza_fibonacci(n)


import random

def quiz(num_problemi):
    punteggio = 0

    for _ in range(num_problemi):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operazione = random.choice(['+', '-', '*', '/'])

        if operazione == '+':
            risultato_corretto = num1 + num2
        elif operazione == '-':
            risultato_corretto = num1 - num2
        elif operazione == '*':
            risultato_corretto = num1 * num2
        else:  # operazione == '/'
            while num2 == 0:
                num2 = random.randint(1, 10)
            risultato_corretto = num1 / num2

        domanda = f"Quanto fa {num1} {operazione} {num2}? "
        risposta_utente = float(input(domanda))

        print("Scossaaaaa?!")
        if risposta_utente == risultato_corretto:
            print("Corretto!")
            punteggio += 1
        else:
            print(f"Sbagliato! La risposta corretta era {risultato_corretto}.")

    print(f"Hai ottenuto {punteggio} risposte corrette su {num_problemi}.")

num_problemi = int(input("Quanti problemi matematici vuoi risolvere? "))
quiz(num_problemi)

# capitalize() - Converts the first character to upper case
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# casefold() - Converts string into lower case
text = "Hello World"
print(text.casefold())  # Output: "hello world"

# center() - Returns a centered string
text = "hello"
print(text.center(10, "-"))  # Output: "--hello---"

# count() - Returns the number of times a specified value occurs in a string
text = "hello world"
print(text.count("o"))  # Output: 2

# endswith() - Returns true if the string ends with the specified value
text = "hello world"
print(text.endswith("world"))  # Output: True

# find() - Searches the string for a specified value and returns the position of where it was found
text = "hello world"
print(text.find("world"))  # Output: 6

# format() - Formats specified values in a string
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# isalpha() - Returns True if all characters in the string are in the alphabet
text = "hello"
print(text.isalpha())  # Output: True

# isdigit() - Returns True if all characters in the string are digits
text = "123"
print(text.isdigit())  # Output: True

# lower() - Converts a string into lower case
text = "Hello World"
print(text.lower())  # Output: "hello world"

# replace() - Returns a string where a specified value is replaced with a specified value
text = "hello world"
print(text.replace("world", "python"))  # Output: "hello python"

# split() - Splits the string at the specified separator, and returns a list
text = "hello world"
print(text.split())  # Output: ['hello', 'world']

# strip() - Returns a trimmed version of the string
text = "   hello world   "
print(text.strip())  # Output: "hello world"

# upper() - Converts a string into upper case
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"

import datetime

# Creare una data
data = datetime.date(2018, 12, 31)
print("Data:", data)

# Ottenere il giorno della settimana
giorno_settimana = data.strftime("%A")
print("Giorno della settimana:", giorno_settimana)

# Ottenere il numero del giorno nell'anno
numero_giorno_anno = data.strftime("%j")
print("Numero del giorno nell'anno:", numero_giorno_anno)

# Ottenere la settimana dell'anno
settimana_anno = data.strftime("%W")
print("Settimana dell'anno:", settimana_anno)

# Ottenere il nome e il numero del mese
nome_mese = data.strftime("%B")
numero_mese = data.strftime("%m")
print("Mese:", nome_mese, "(", numero_mese, ")")

# Creiamo un oggetto datetime con una data specifica (ad esempio: 2024-05-29)
x = datetime.datetime(2024, 5, 29)

# Utilizziamo il metodo strftime per ottenere l'abbreviazione del giorno della settimana
print(x.strftime("%a"))  # Output: Tue (Martedì)
import datetime

# Creiamo un oggetto datetime con una data specifica (ad esempio: 2024-05-29)
x = datetime.datetime(2024, 5, 29)

# Utilizziamo il metodo strftime per ottenere il nome abbreviato del mese
print(x.strftime("%b"))  # Output: May (Maggio)

# Formattare la data
data_formattata = data.strftime("%Y-%m-%d")
print("Data formattata:", data_formattata)

# Aggiungere o sottrarre giorni
nuova_data = data + datetime.timedelta(days=5)
print("Nuova data (aggiungendo 5 giorni):", nuova_data)

# Ottenere la data e l'ora corrente
data_ora_corrente = datetime.datetime.now()
print("Data e ora correnti:", data_ora_corrente)

# Ottenere solo l'ora corrente
ora_corrente = data_ora_corrente.strftime("%H:%M:%S")
print("Ora corrente:", ora_corrente)


#Ciclo while

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Salta l'iterazione corrente se i è uguale a 3
    print(i)  # Stampa il valore di i

    if i == 5:
        break  # Esce dal ciclo se i è uguale a 5

else:
    print("Il ciclo è terminato senza incontrare il break.")  # Stampato se il ciclo termina normalmente


#Ciclo For 

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break  # Se il valore corrente è "banana", esce dal ciclo
    if x == "cherry":
        continue  # Se il valore corrente è "cherry", salta il resto del blocco e passa alla prossima iterazione
    print(x)  # Stampa il valore corrente

else:
    print("Il ciclo è terminato senza incontrare il break.")  # Stampa se il ciclo termina normalmente senza l'uso di break


