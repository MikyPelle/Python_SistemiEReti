import random
class Nemici():
    def __init__(self, posizione_x, posizione_y, n_vite):
        self.posizione_x = posizione_x
        self.posizione_y = posizione_y
        self.n_vite = n_vite
    
    def stampa(self):
        print(f"Nemico in posizione {self.posizione_x}, {self.posizione_y} con {self.n_vite} vite")
        
def main():
    N_NEMICI = 5
    HEIGHT = 400
    WIDTH = 800
    lista_nemici = []
    for _ in range(N_NEMICI):
        pos_x = random.randint(0, WIDTH-1)
        pos_y = random.randint(0, HEIGHT-1)
        nemico = Nemici(pos_x, pos_y, 5)
        lista_nemici.append(nemico)
    print(lista_nemici)
    
    personaggio = {"posizione_x":100, "posizione_y":200}
    for nemico in lista_nemici:
        nemico.stampa()
    if nemico.posizione_x == personaggio["posizione_x"] and nemico.posizione_y == personaggio["posizione_y"]:
        print("COLLISIONE")

if __name__ == "__main__":
    main()