import turtle
def main():
    
    nLati = int(input("inserisci il numero di lati: "))

    finestra = turtle.Screen()
    sciolla = turtle.Turtle()

    sciolla.begin_fill()

    for i in range(0, nLati):
        sciolla.color('red')
        sciolla.forward(100)
        sciolla.left(360 / nLati)
        
    sciolla.end_fill()

    finestra.mainloop()
    
if __name__ == "__main__":
    main()