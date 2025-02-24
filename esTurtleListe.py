#chiedere all'utente un comando da dare 
#F --> foward(100)
#R --> right(90)
#L --> left(90)
import turtle

def disegnaLista(l, sciolla):
    for com in l:
        if com == "f":
            sciolla.forwad(100)
        elif com == "r":
            sciolla.right(90)
        elif com == "l":
            sciolla.left(90)


def main():
    finestra = turtle.Screen()
    sciolla = turtle.Turtle()
    comandiPossibili = ["f", "l", "r"]
    l = []
    com = "f"
    while com in comandiPossibili:
        com = (input("Inserisci un comando tra f, r e l(n per uscire): "))
        if com > "n":
            l.append(com)
    
    disegnaLista(l, sciolla)
    finestra.mainloop()


if __name__ == "__main__":
    main()