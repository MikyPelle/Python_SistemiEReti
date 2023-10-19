import turtle
def main():
    n = int(input("inserisci il numero delle punte della stella: "))
    
    finestra = turtle.Screen()
    sciolla = turtle.Turtle()
    sciolla.color("red")

    angolo = 360 / n
    sciolla.speed(10)

    sciolla.begin_fill()
    for i in range(n):
        sciolla.forward(100)
        sciolla.right(180 - angolo)
    sciolla.end_fill()    

    finestra.mainloop()
    
if __name__ == "__main__":
    main()