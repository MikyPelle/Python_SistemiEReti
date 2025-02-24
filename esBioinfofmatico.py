def contaLettere(c, genoma):
    return len([x for x in genoma if x == c])

def cercaStringa(genoma):
    stringa = "ATGTTTGTTTTT"
    for i, _ in enumerate(genoma[:-12]):
        if genoma[i:i+len(stringa)] == stringa:
            return i
    return -1

def main():
    genoma = ""
    f = open("covid-19_gen1.txt", "r")
    for riga in f.readlines():
        genoma += riga[:-1]
    f.close()
    
    print(f"A: {contaLettere('A', genoma)}\nC: {contaLettere('C', genoma)}\nG: {contaLettere('G', genoma)}\nT: {contaLettere('T', genoma)}")
    
    print(f"stringa 'ATGTTTGTTTTT' in posizione: {genoma.find('ATGTTTGTTTTT')}")
    print(f"stringa 'ATGTTTGTTTTT' in posizione: {cercaStringa(genoma)}")
    
if __name__ == "__main__":
    main()