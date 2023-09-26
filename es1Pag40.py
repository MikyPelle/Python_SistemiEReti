def main():
    x = int(input("inserisci un numero: "))

    if x % 3 == 0:
        print(f"è divisibile per 3.")
    else:
        print(f"non è divisibile per 3.")


if __name__ == "__main__":
    main()