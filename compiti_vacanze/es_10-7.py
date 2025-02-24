def ha_duplicati(lista):
    visti = []
    for elemento in lista:
        if elemento in visti:
            return True
        visti.append(elemento)
    return False

def main():
    lista = ["ciao", "cielo"]
    if ha_duplicati(lista):
        print("La lista ha duplicati")
    else:
        print("La lista non ha duplicati")
        
if __name__ == '__main__':
    main()