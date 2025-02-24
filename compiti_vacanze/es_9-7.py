def tre_doppie(parola):
    cont = 0
    i = 0
    while i < len(parola) - 1:
        if parola[i] == parola[i + 1]:
            cont += 1
            i += 2 
            if cont == 3:
                return True
        else:
            cont = 0
            i += 1
    return False

def main():
    parola = input("Inserire una parola: ")
    if tre_doppie(parola):
        print("La parola ha 3 lettere consecutive uguali")
    else:
        print("La parola non ha 3 lettere consecutive uguali")
if __name__ == '__main__':
    main()