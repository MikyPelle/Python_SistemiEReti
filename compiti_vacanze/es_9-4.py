def usa_solo(parola,lettere_ammesse):
    for lettera in parola:
        if lettera not in lettere_ammesse:
            return False
    return True
    
def main():
    lettere_ammesse = input("Inserire le lettere da ammettere: ").strip()
    parola = input("Inserire una parola: ")
    if usa_solo(parola, lettere_ammesse):
        print("La parola contiene solo le lettere ammesse")
    else:
        print("La parola contine lettere non ammesse")
if __name__ == '__main__':
    main()