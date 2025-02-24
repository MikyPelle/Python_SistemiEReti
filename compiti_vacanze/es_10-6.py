def anagramma(parola1, parola2):
    return sorted(parola1) == sorted(parola2)

def main():
    if anagramma('parte', 'perta'):
        print("Anagramma trovato")
    else:
        print("Anagramma non trovato")

if __name__ == "__main__":
    main()
