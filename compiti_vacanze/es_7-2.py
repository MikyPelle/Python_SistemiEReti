def eval_ciclo():
    ultimo_ris = None
    while True:
        print("inserisci un'espressione numerica ['fatto' per terminare]")
        strg = input("> ")
        if strg.lower() == "fatto": #se ci sono maiuscole vengono convertite in minuscole per evitare errori
            return ultimo_ris
        ultimo_ris = eval(strg)
def main():
    ris = eval_ciclo()
    if ris is not None:
        print(f"l'ultimo risultato è {ris}")
    else:
        print("nessun risultato trovato")
if "__main__" == __name__:
    main()