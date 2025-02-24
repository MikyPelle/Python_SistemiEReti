def somma_cumulata(lista):
    somma = 0
    lista_cumulata = []
    for num in lista:
        somma += num
        lista_cumulata.append(somma)
    return lista_cumulata

def main():
    l = [1,2,3]
    print(somma_cumulata(l)) 

if __name__ == "__main__":
    main()