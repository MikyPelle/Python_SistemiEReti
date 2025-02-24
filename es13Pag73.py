class Robot:
    def __init__(self, nome, massa, umanoide):
        self.nome = nome
        self.massa = massa
        self.umanoide = umanoide

    def stampa_nome(self):
        print(f"Nome del robot: {self.nome}")

    def is_pericoloso(self):
        if self.umanoide and self.massa > 100:
            return True
        else:
            return False

def main():
    nome = input("Inserisci il nome del robot: ")
    massa = int(input("Inserisci la massa del robot: "))
    umanoide = input("è umanoide? [si/no]: ")
    
    if umanoide == "si":
        robot = Robot(nome, massa, True)
    elif umanoide == "no":
        robot = Robot(nome, massa, False)
    else:
        print("Errore nell'inserimento dati")
        
    
    if umanoide == "si" or umanoide == "no":
        robot.stampa_nome()
        if robot.is_pericoloso():
            print(f"Il robot {robot.nome} è pericoloso.")
        else:
            print(f"Il robot {robot.nome} non è pericoloso.")
        
if __name__ == "__main__":
    main()