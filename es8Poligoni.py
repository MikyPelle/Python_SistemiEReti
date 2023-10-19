import turtle

def disegnaPoligono(s, num, lato):
    #disegno poligono
    gradi = 360 / num
    s.begin_fill()
    for i in range (0, num):
        s.forward(lato)
        s.left(gradi)
    s.end_fill()

def posizionaTurtle(s, x, y, lato, num):
    if (num % 3 == 0):
        x = -200
        y = y + lato * 4
    else:
        x = x + lato * 4
    return x, y

def main():
    x = 0
    y = -350
    lato = 40
    finestra = turtle.Screen()
    sciolla = turtle.Turtle()
    sciolla.shape("turtle")
    sciolla.color("red")
    sciolla.speed(10)

    for num in range(3, 12):
        #posiziono la turtle prima di disegnare il poligono
        sciolla.penup()
        x, y = posizionaTurtle(sciolla, x, y, lato, num)
        sciolla.goto(x,y)
        sciolla.pendown()
        disegnaPoligono(sciolla, num, lato)
    finestra.mainloop()


if __name__ == "__main__":
    main()