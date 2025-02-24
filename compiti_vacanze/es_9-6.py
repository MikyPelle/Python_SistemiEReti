def alfabetica(parola):    
    i = 0
    while i < len(parola)-1:
        if parola[i+1] < parola[i]:
            return False
        i = i+1
    return True

def main():
    parola = input("Inserisci una parola: ")
    if alfabetica(parola):
        print("Le lettere della parola sono in ordine alfabetico")
    else:
        print("Le lettere della parola non sono in ordine alfabetico")

if __name__ == '__main__':
    main()
