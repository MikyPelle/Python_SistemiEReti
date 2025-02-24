def bifronte(lista):
    bif = []
    for el in range(len(lista)):
        reverse = lista[el][::-1]
        if reverse in lista:
            bif.append(reverse)
    return bif

def main():
    lista = ["ciao","oaic","bravo","ovarb"]
    print(bifronte(lista))
    
if __name__ == '__main__':
    main()