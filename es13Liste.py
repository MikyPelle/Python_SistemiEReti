#List comprension
import random
quadrati = [i*i for i in range(1, 6)] #Lista con i primi 5 quadrati perfetti
numeri_interi = [i for i in range(1, 11)] #Lista con i primi dieci numeri
print(quadrati)
print(numeri_interi)

stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = [parola for parola in stringhe if parola[0] == "c"] # cerca le parole nella lista che iniziano con c
print(stringhe_c)

voti = [random.randint(2, 10) for _ in range(0, 10)] #Inizializza dieci voti random
print(voti)                     #Si usa _ al posto di una variabile che non viene utilizzata ma deve esserci 
                                #non occupa spazio in memoria
voti_insuff = [voto for voto in voti if voto < 6]
print(voti_insuff)