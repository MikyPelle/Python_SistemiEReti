import random
 
def main():
    lista_spostamenti = [random.choice([1, -1]) for _ in range(60 * 60 * 24 * 5)]
    somma = 0
    for i in lista_spostamenti:
        somma += i
    print(f"si è spostato di {somma}cm")

    
if __name__ == "__main__":
    main()