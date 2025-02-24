def somma_nid(liste_nid):
    somma_totale = 0
    for sotto_lista in liste_nid:
        somma_totale += sum(sotto_lista)
    return somma_totale

def main():
    l = [[1,2,3],[5],[8,9,10]]
    print(somma_nid(l))

if __name__ == "__main__":
    main()