def evita(word,lettere_vietate):
    vietato = False
    for lettera in lettere_vietate:
        if lettera in word:
            vietato = True
    return vietato
    
def main():
    lettere_vietate = input("Inserisci una stringa di lettere vietate: ").strip()
    word = input("Inserire una parola: ")
    if evita(word, lettere_vietate):
        print("La parola contiene lettere vietate")
    else:
        print("La parola non contiene lettere vietate")
if __name__ == '__main__':
    main()