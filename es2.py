def main():
    a = float(input("inserisci un numero: "))
    print(f"il tipo di a è {type(a)}")
    if a > 5:
        print("a è maggiore di 5")
    elif (a<=5) and (a>=0):
        print("a è minore o uguale a 0 e maggiore o uguale a 0")
    else:
        print("a è minore di 0")

if __name__ == "__main__":
    main()