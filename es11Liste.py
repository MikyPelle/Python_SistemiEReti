def print_list(l):
    print("La lista è: ", end=" ")
    for elemento in l:
        print(elemento, end=" ")    #end è un parametro che si può passare alla funzione print si può cambiare l'ultimo
    print("\n")

def main():
    #Le liste
    l = [1, 2, 3, 4, "c", 3.14, "python"]
    r = [10, 11, 12]
    print_list(l + r)   #concatena le liste l e r
    print_list(3*r) #stampa 3 volte la lista r
    #print(l)
    print_list(l[::-1])

    #vogliamo permettere all'utente di caricare una lista
    lista = []
    num = 1
    while num > 0:
        num = int(input("Scrivi un numero: (-1 per interrompere): "))
        
        if num > 0:
            lista.append(num)   #append è un metodo che permettere di aggiungere qualcosa alla lista
    print(lista)


if __name__ == "__main__":
    main()