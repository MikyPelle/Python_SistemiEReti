def main():
    op = int(input("Scegliere l'operazione:\n0: somma\n1: sottrazione\n2: moltiplicazione\n3: divisione     :"))
    x = int(input("inserisci un numero: "))
    y = int(input("inserisci un altro numero: "))

    if op == 0:
        ris = x + y
    elif op == 1:
        ris = x - y
    elif op == 2:
        ris = x * y
    elif op == 3:
        if y == 0:
            print(f"non si può dividere per 0")
            exit(1)
        else:
            ris = x / y
    else:
        print(f"operazione inserita non valida")

    if (op >= 0) and (op <= 3):
        print(f"risultato = {ris}")


if __name__ == "__main__":
    main()