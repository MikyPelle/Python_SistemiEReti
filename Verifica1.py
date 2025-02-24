class Testo():
    def __init__(self, testo):
        self.testo = testo
    def n_caratteri(self):
        n_car = 0
        for i in self.testo:
            if i != " ":
                n_car += 1
        return n_car
        #return len(self.testo) più corto
    def lista_parole(self):
        lista_parole = self.testo.split(" ")
        return lista_parole
        #return self.testo.split(" ") più corto
    def lung_parole(self):
        lista_parole = self.lista_parole()
        lista_lung = [len(i) for i in lista_parole]
        return lista_lung
    def cerca_parola(self, parola):
        tro = False
        lista_parole = self.lista_parole()
        if parola in lista_parole:
            tro = True
        return tro
        #return parola in lista_parole --> ritorna un booleano
    def salva_su_file(self, nome_file):
        with open(nome_file, "w") as f:
            f.write(self.testo)
            
    #da guardare!!!
    def frequeze_parole(self):
        frequenze = {}
        for parola in self.lista_parole():
            if parola in frequenze:
                frequenze[parola] += 1
            else:
                frequenze[parola] = 1
        return frequenze
    
def main():
    frase = "oggi è una bella giornata"
    testo = Testo(frase)
    print(testo.n_caratteri())
    print(testo.lista_parole())
    print(testo.lung_parole())
    
    parola = "bella"
    if testo.cerca_parola(parola):
        print(f"{parola} è presente nella frase")
    else:
        print(f"{parola} non è presente nella frase")
    parola2 = "ciao"
    if testo.cerca_parola(parola2):
        print(f"{parola2} è presente nella frase")
    else:
        print(f"{parola2} non è presente nella frase")
        
    nome_file = "testo.txt"
    testo.salva_su_file(nome_file)
    print(testo.frequeze_parole())
        
if __name__ == "__main__":
    main()