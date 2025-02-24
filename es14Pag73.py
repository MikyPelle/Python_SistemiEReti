class Quadrato:
    def __init__(self, lato):
        self.lato = lato

    def calcola_area(self):
        return self.lato ** 2

    def calcola_perimetro(self): 
        return 4 * self.lato

    def punto_interno(self, x, y):
        if (x > 0 and x < self.lato and y > 0 and y < self.lato):
            return True
        else: 
            return False

def main():
    lato = int(input("Inserisci la lunghezza del lato: "))
    quadrato = Quadrato(lato)

    area = quadrato.calcola_area()
    perimetro = quadrato.calcola_perimetro()

    print(f"Area del quadrato: {area}")
    print(f"Perimetro del quadrato: {perimetro}")

    x = int(input("Inserisci le coordinate x del punto: "))
    y = int(input("Inserisci le coordinate y del punto: "))
    
    if quadrato.punto_interno(x, y):
        print(f"Il punto ({x}, {y}) è all'interno al quadrato.")
    else:
        print(f"Il punto ({x}, {y}) è esterno del quadrato.")

if __name__ == "__main__":
    main()