#print va a capo da solo
#input è una stringas
#si può vedere il tipo di una variabile con il comando print(type(nome variabile))
def main():#indentando si creano dei blocchi
    nome = input("Come ti chiami?")
    anni = int(input("Quanti anni hai?"))
    anno_corrente = int(input("In quale anno siamo?"))
    print(f"Il tuo nome è {nome} e hai {anni} anni")
    print(f"sei nato nel {anno_corrente - anni}")

if __name__ == "__main__":  #doppio underscore (doubleunder) -> dunder
    main()
