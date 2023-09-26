def main():
    x = int(input("inserisci un numero: "))

    if x % 2 == 0:
        print(f"è divisibile per 2.")
    elif x % 3 == 0:
        print(f"è divisibile per 3.")
    elif x % 5 == 0:
        print(f"è divisibile per 5.")
    else:
        print(f"non si può dividere ne per 2 ne per 3  ne per 5.")


if __name__ == "__main__":
    main()