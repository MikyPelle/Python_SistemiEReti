class Coda():
    def __init__(self):
        self.lista = []
    def is_empty(self):
        return self.lista == []
    def enqueue(self, elemento):
        self.lista.append(elemento)
    def dequeue(self):
        if self.is_empty():
            print("Coda vuota")
        else:
            return self.lista.pop()
        return None
    def stampa(self):
        print(self.lista)

def main():
    c = Coda()
    c.enqueue(10)
    c.enqueue(2)
    print(f"elemento rimosso: {c.dequeue()}")
    c.stampa() 
    
if __name__ == "__main__":
    main()