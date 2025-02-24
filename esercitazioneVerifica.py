import turtle
import random

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def nord(bob):
    bob.setheading(90)
    bob.forward(10)

def sud(bob):
    bob.setheading(270)
    bob.forward(10)

def est(bob):
    bob.setheading(0)
    bob.forward(10)

def ovest(bob):
    bob.setheading(180)
    bob.forward(10)

def main():
    dizionario = {"n": nord, "s": sud, "e": est, "o": ovest}
    possibiliCaratteri = ["n", "s", "o", "e"]
    percorso = {0: Punto(0, 0)}
    casa_x = 100
    casa_y = 50
    finestra = turtle.Screen()
    bob = turtle.Turtle()
    bob.speed(0)
    for tempo in range(1, 60):
        # simulare movimenti casuali
        direzione = random.choice(possibiliCaratteri)
        # disegnare percorso con turtle
        dizionario[direzione](bob)
        percorso[tempo] = Punto(bob.xcor(), bob.ycor())
        # BONUS controllo passaggio punto già visitato
        if percorso[tempo].x == percorso[tempo - 1].x and percorso[tempo].y == percorso[tempo - 1].y:
            print(f"bob è passato di nuovo in ({percorso[tempo].x},{percorso[tempo - 1]})")
        if casa_x == bob.xcor() and casa_y == bob.ycor():
            print("Casa trovata!")
            break

    # scrittura su file del percorso
    # COLONNE: minuto, x, y
    with open("percorso.csv", "w") as file:
        # ciclo sul dizionario
        for minuto in percorso:
            posx = int(percorso[minuto].x)
            posy = int(percorso[minuto].y)
            file.write(f"{minuto}, {posx}, {posy}\n")

    finestra.mainloop()
    
if __name__ == "__main__":
    main()