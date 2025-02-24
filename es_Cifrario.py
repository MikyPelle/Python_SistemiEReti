class Testo():
    def _init_(self, stringa, chiave, cifrato):
        self.stringa = stringa.lower() 
        self.chiave = chiave.lower() 
        self.cifrato = cifrato #bool
        self.cifra = []
        self.decifra = []
                
    def cifra_cod(self, dizio):
        if self.cifrato == False:
            lista_chiave = [c for c in self.chiave]
            for indice,char in enumerate(self.stringa):
                # prendo entrambi dallo stesso diz per avere la chiave in numero
                self.cifra.append((dizio[char] + dizio[lista_chiave[indice]]) % 21)
            self.cifrato = True
            print(",".join(str(c) for c in self.cifra))#la virgola per separare i numeri
        else:
            print("la stringa è già cifrata")
    
    def decifra_cod(self, dizio, diz_num):
        if self.cifrato == True:
            lista_chiave = [c for c in self.chiave]
            for indice,elem in enumerate(self.cifra):
                #prendo una dalla chiave e l'altro da dove le chiavi sono le lettere 
                #per avere entrambi in numeri a cui dopo faccio l'append a quello con le lettere
                self.decifra.append(dizio[(elem - diz_num[lista_chiave[indice]]) % 21])
            self.cifrato = False
            print("".join(c for c in self.decifra))#qua non serve la , perchè sono lettere
        else:
            print("la stringa è già decifrata")
        
def main():
    diz_par = {0: 'a',1: 'b',2: 'c',3: 'd',4:'e',5: 'f',
                  6: 'g',7: 'h',8: 'i',9: 'l',10: 'm',11: 'n',12:'o', 
                  13: 'p',14: 'q',15: 'r',16: 's',17: 't',18: 'u',19: 'v',20: 'z'}
    
    diz_num = {} # i numeri sono il contenuto mentre i char la chiave
    
    for chiave in diz_par:
        diz_num[diz_par[chiave]] = chiave
        
    parola = input("inserisci una parola: ")
    testo = Testo(parola, "abcdefghijkl" , False)
    testo.cifra_cod(diz_num)
    testo.decifra_cod(diz_par, diz_num)

if __name__ == "__main__":
    main()