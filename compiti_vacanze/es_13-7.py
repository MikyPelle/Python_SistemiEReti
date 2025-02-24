import random
import string

def pulisci_parola(parola):
    rimuovibili = string.punctuation + string.whitespace
    parola = parola.strip(rimuovibili).lower()
    return parola


def process_book(file):
    num_parole = {}
    inizia = False

    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            if '*** START OF THE PROJECT GUTENBERG EBOOK MOBY DICK; OR, THE WHALE ***' in line:
                inizia = True
                continue
            if '*** END OF THE PROJECT GUTENBERG EBOOK MOBY DICK; OR, THE WHALE ***' in line:
                break

            if inizia:
                parole = line.split()
                for parola in parole:
                    parola_pulita = pulisci_parola(parola)
                    if parola_pulita:
                        num_parole[parola_pulita] = num_parole.get(parola_pulita, 0) + 1

    return num_parole

def parola_caso(h):
    t = []
    for parola, freq in h.items():
        t.extend([parola] * freq)
    return random.choice(t)

def main():

    file = "Moby_Dick_gutenberg.txt"  
    num_parole = process_book(file)
    parola_scelta = parola_caso(num_parole)
    
    print("La parola scelta a caso è:", parola_scelta)

if __name__ == '__main__':
    main()
