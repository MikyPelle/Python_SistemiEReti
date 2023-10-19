# SLICING (DIVIDERE) DI STRINGHE
s = "ciao come stai?" #in python si può indicizzare in un modo diverso da 0 1 2 3 --> -4 -3 -2 -1 
           #si parte dall'ultima cella
print(f"Il primo carattere è {s[0]}")
print(f"L'ultimo carattere è {s[-1]}")
print(f"Il penultimo carattere è {s[-2]}")
print(f"L'ultimo carattere è {s[len(s) - 1]}")#C-style DA NON USARE!!
print(s[3:7])#dal carattere 3 al 7 esculso
print(f"Tutta la stringa esculsi primo e ultimo carattere: {s[1:-1]}")
print(f"Tutta la stringa esculso il primo carattere: {s[1:]}")
print(f"Tutta la stringa esculso l'ultimo carattere: {s[:-1]}")
print(s[::-1])#stampa la stringa al contrario