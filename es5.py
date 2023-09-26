def main():
    lista = [4, 100, 3, 5, "ciao", print]#lista

    #Ciclo for C-style
    for i in range (0, len(lista)):
        print(f"L'elemento {i}-esimo della lista è: {lista[i]}")
    
    #Ciclo for Python-style
    for elemento in lista:
        print(f"Elemento: {elemento}")




if __name__ == "__main__":
    main()