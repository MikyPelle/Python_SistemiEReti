def prodotto(a, b):
    return a * b

def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def divisione(a, b):
    return a / b

def main():
    #pass #non fa nulla 
    dizionario = {"+": somma, "*":  prodotto, "-": sottrazione, "/": divisione}
    operazione = input("Scrivi + per somma, * per prodotto, - per sottrazione e / per divisione: ")
    a = float(input("Scrivi il primo numero: "))
    b = float(input("Scrivi il secondo numero: "))
    print(dizionario[operazione](a, b))   
    
    
if __name__ == "__main__":
    main()