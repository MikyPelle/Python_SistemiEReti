def eliminaVocali(s):
    vocali = "aeiouAEIOU"    
    sSenzaVoc = [c for c in s if c not in vocali]
    return sSenzaVoc
    

def main():
    s = "ciao"
    sSenzaVoc = eliminaVocali(s)
    print("".join(sSenzaVoc))
    
if __name__ == "__main__":
    main()