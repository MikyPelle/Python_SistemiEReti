def completa8bit(strbin):
    l = len(strbin)
    return "0" * (8 - l) + strbin

def main():
    address = input("Inserisci in indirizzo ip: ")
    groups = address.split(".")#spezza la stringa con un carattere ricorrente 
    groups = [int(group) for group in groups]
    print(groups)
    groups_bin = [bin(group)[2:] for group in groups]
    print(groups_bin)
    print(completa8bit(groups_bin[k] for k in range(0, 4)))
    print("ciao" .join(groups_bin))#scrive quello tra parentesi dopo ogni gruppo è "l'opposto di split"
    
if __name__ == "__main__":
    main()