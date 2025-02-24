import string

def pulisci_parola(parola):
    rimuovibili = string.punctuation + string.whitespace
    parola = parola.strip(rimuovibili).lower()
    return parola

def carica_elenco_parole(file):
    elenco_parole = set()
    with open(file, 'r', encoding='utf-8') as file:
        for riga in file:
            parola = pulisci_parola(riga)
            if parola:
                elenco_parole.add(parola)
    return elenco_parole

def processa_libro(file):
    conteggio_parole = {}
    inizia = False

    with open(file, 'r', encoding='utf-8') as file:
        for riga in file:
            if '*** START OF THE PROJECT GUTENBERG EBOOK MOBY DICK; OR, THE WHALE ***' in riga:
                inizia = True
                continue
            if '*** END OF THE PROJECT GUTENBERG EBOOK MOBY DICK; OR, THE WHALE ***' in riga:
                break

            if inizia:
                parole = riga.split()
                for parola in parole:
                    parola_pulita = pulisci_parola(parola)
                    if parola_pulita:
                        conteggio_parole[parola_pulita] = conteggio_parole.get(parola_pulita, 0) + 1

    return conteggio_parole

def trova_parole_sconosciute(conteggio_parole_libro, elenco_parole):
    parole_sconosciute = conteggio_parole_libro.keys() - elenco_parole
    return parole_sconosciute

def main():
    libro = "Moby_Dick_gutenberg.txt"
    elenco = "elenco_parole.txt"
    elenco_parole = carica_elenco_parole(elenco)
    conteggio_parole_libro = processa_libro(libro)
    parole_sconosciute = trova_parole_sconosciute(conteggio_parole_libro, elenco_parole)
    print(f"Parole sconosciute: {len(parole_sconosciute)}")
    print(parole_sconosciute)

if __name__ == "__main__":
    main()
