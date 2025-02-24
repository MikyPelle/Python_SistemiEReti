import turtle

def spostamento(sciolla, x, y):
    sciolla.penup()
    sciolla.goto(x, y)
    sciolla.pendown()
    
def main():
    finestra = turtle.Screen()
    sciolla = turtle.Turtle()
    x, y, lato = -70, 70, 50
    spostamento(sciolla, x, y)
    sciolla.speed(0)
    for _ in range(0, 5):
        sciolla.forward(lato * 4)
        y -= lato
        spostamento(sciolla, x, y)
        
    sciolla.right(90)
    y += lato * 5
    spostamento(sciolla, x, y)
    for _ in range(0, 5):
        sciolla.forward(lato * 4)
        x += lato
        spostamento(sciolla, x, y)
        
    finestra.mainloop()

if __name__ == "__main__":
    main()