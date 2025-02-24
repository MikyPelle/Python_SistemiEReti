def main():
    lista = [6, 6, 8, 5, 9, 3, 7, 10]
    
    print(lista[1:-1])
    
    lista[4] = 10
        
    print(lista[:3])

def main1():
    lista = []
    k = 0
    
    while True:
        voto = int(input("Inserisci un voto: -1 per interrompere: "))
        if(voto < 0 and k >= 6):
            break
        lista.append(voto)
        k += 1
    print(lista[1:-1])
    
    lista[4] = 10
        
    print(lista[:3])
        
        
if __name__ == "__main__":
    main()
    main1()