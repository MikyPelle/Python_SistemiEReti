def main():
    n = int(input("Inserisci una cdr per la subnet mask (tra 0 e 31): "))
    str = "1" * n + "0" * (32 - n)
    print(str)
    gruppo1 = int(str[0:8], 2)
    gruppo2 = int(str[8:16], 2)
    gruppo3 = int(str[16:24], 2)
    gruppo4 = int(str[24:], 2)
    lista = f"{gruppo1}.{gruppo2}.{gruppo3}.{gruppo4}"
    print(lista)    
    
if __name__ == "__main__":
    main()