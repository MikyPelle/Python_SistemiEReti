import math
def main():
    n = int(input("Inserisci un numero come limite per le potenze di 2: "))
    esponente = int(math.log2(n))
    l = [2**i for i in range(0, esponente + 1) if 2**i <= n]
    print(l)
    
    
if __name__ == "__main__":
    main()