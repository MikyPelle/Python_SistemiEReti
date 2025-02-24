lettere = "abcdefghijklmnopqrstuvz ?!"
n = len(lettere)
lettere2numeri = {}
numeri2lettere = {}

for posizione, lettera in enumerate(lettere):
    lettere2numeri[lettera] = posizione     #riempio i dizionari
    numeri2lettere[posizione] = lettera    

testo_chiaro = "ciao come stai ?"
chiave = "itisdelpozzo kinceu ciwvewu?"
testo_criptato = ""

for lettera_testo,lettera_chiave in zip(testo_chiaro, chiave):
    numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave]) % n
    testo_criptato = testo_criptato + numeri2lettere[numero]
print(f"il testo '{testo_chiaro}' diventa: '{testo_criptato}'.")

testo_chiaro = ""

for numero_testo,numero_chiave in zip(testo_criptato, chiave):
    lettera = (numeri2lettere[numero_testo] + numeri2lettere[numero_chiave]) % n
    testo_chiaro = testo_chiaro + lettere2numeri[lettera]
print(f"il testo '{testo_criptato}' diventa: '{testo_chiaro}'.")

"""for lettera in testo_chiaro:
    print(lettere2numeri[lettera]) #cerca cos'è la chiave lettera e stampa il valore associato ad essa"""