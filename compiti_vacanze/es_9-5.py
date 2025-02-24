def usa_tutte(parola, lettere_richieste):
    for lettera in lettere_richieste:
        if lettera not in parola:
            return False
    return True

def main():
    lettere_richieste = input("Inserisci le lettere richieste: ").strip()
    parola = input("Inserisci una parola: ")
    if usa_tutte(parola, lettere_richieste):
        print("La parola utilizza tutte le lettere richieste almeno una volta.")
    else:
        print("La parola non utilizza tutte le lettere richieste.")

if __name__ == '__main__':
    main()
