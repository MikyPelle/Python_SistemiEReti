import turtle

def nord(sciolla):
    sciolla.setheading(90)
    sciolla.forward(100)

def sud(sciolla):
    sciolla.setheading(270)
    sciolla.forward(100)

def est(sciolla):
    sciolla.setheading(0)
    sciolla.forward(100)

def ovest(sciolla):
    sciolla.setheading(180)
    sciolla.forward(100)

def exit(sciolla):
    return exit

def main(): 
    finestra = turtle.Screen()
    sciolla = turtle.Turtle()

    dizionario = {"n": nord, "s": sud, "e": est, "o": ovest, "exit": exit}
    while(True):
        operazione = input("Scrivi n per nord, s per sud, e per est, o per ovest e exit per uscire: ")
        if operazione in dizionario:
            print(dizionario[operazione](sciolla))
        else:
            print("Errore")  
        finestra.mainloop()
    
    
if __name__ == "__main__":
    main()