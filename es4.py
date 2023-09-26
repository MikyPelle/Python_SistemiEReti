def main():
    x = int(input("inserisci un numero: "))
    y = int(input("inserisci un altro numero: "))

    if x > y:
        x, y = y, x #scambio x con y e viceversa
        #assegnamento multiplo int a, b = 5, 7
    
    print(f"{x} {y}")

if __name__ == "__main__":
    main()