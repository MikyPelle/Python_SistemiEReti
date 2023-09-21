def main():
    num1 = int(input("inserisci un numero: "))
    num2 = int(input("inserisci un altro numero: "))

    if num1 > num2:
        num1, num2 = num2, num1
    
    print(f"{num1} {num2}")

if __name__ == "__main__":
    main()