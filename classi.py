#in python tutto è public, non sono necessari get e set
class Quadrato():
    #self simile al this di java
    def __init__(self, lato):   #costruttore il nome è uguale per tutte le classi
        self.lato = lato
        
    def calcolaArea(self):  #metodo
        return self.lato**2
    
    def stampaLato(self):
        print(f"Il lato è {self.lato}")
    
def main():
    q = Quadrato(4)
    print(f"L'area del quadrato q è {q.calcolaArea()}")
    
if __name__ == "__main__":
    main()