def bisezione(lista, valore):
    inizio, fine = 0, len(lista) - 1
    while inizio <= fine:
        medio = (inizio + fine) // 2
        if lista[medio] == valore:
            return True
        elif lista[medio] < valore:
            inizio = medio + 1
        else:
            fine = medio - 1
    return False

def main():
    parole = ['torre', 'cassa', 'ruota', 'mesi'] 
    if bisezione(parole, 'cassa'):
        print("Elemento presente")
    else:
        print("Elemento non presente")
        
    if bisezione(parole, 'giorni'):
        print("Elemento presente")
    else:
        print("Elemento non presente")

if __name__ == "__main__":
    main()
