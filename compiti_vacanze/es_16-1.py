class Tempo:
    def __init__(self, tempo):
        self.tempo = tempo
        
def moltiplica_temp(tempo, n):
    return tempo.tempo * n

def moltiplica_temp_gara(tempo, n):
    return tempo.tempo/n

def main():
    t = Tempo(50)
    n = 50
    print(moltiplica_temp(t, n))
    print(f"Sono stati percorsi {n} km in {t.tempo} con un valore di {moltiplica_temp_gara(t,n)} al km ")
if __name__ == '__main__':
    main()

