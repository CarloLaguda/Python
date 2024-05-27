# main_Laguda.py
# @author: Laguda Carlo
# Classe: 3F
# Data: 27/05/2024
# Versione: 1.0.2

import datetime
from studente_Laguda import Studente

def main():
    today = datetime.datetime.today().strftime('%d/%m/%Y')
    print("Buongiorno, oggi è il " + today + ". Inserisci le seguenti informazioni per intestare la tua pagella.")

    studente = Studente()
    studente.chiedi_nome()
    studente.chiedi_cognome()
    studente.chiedi_nomeIstituto()
    studente.chiedi_classe()
    studente.chiedi_Eta()
    studente.chiedi_AnnoIscrizione()
    studente.stampa_scheda_utente()

if __name__ == "__main__":
    main()
