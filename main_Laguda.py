# @author: Laguda Carlo
# Classe: 3F
# Data: 27/05/2024
# Versione: 1.0.2

import datetime
from autousate_Laguda import AutoUsate

today = datetime.datetime.today().strftime('%d/%m/%Y')
print("Buongiorno, oggi è il", today)
print("inserisci le seguenti informazioni per inserire l'annuncio di vendita del tuo veicolo usato.")

auto_usate = AutoUsate()
auto_usate.chiedi_nome()
auto_usate.chiedi_cognome()
auto_usate.chiedi_modello()
auto_usate.chiedi_marca()
auto_usate.chiedi_anno_immatricolazione()
auto_usate.chiedi_prezzo_vendita()
auto_usate.stampa_schede()

