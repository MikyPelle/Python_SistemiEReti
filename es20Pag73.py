"""def main():
    f = open("tavolaPitagorica.csv", 'w')
    for i in range(1, 10 + 1):
        for j in range(1, 10 + 1):
            f.write(f"{i * j}    ")
        f.write(f"\n")
    f.close()"""
    
def main():
    l = [[k*i for i in range(1, 11)] for k in range(1, 11)]
    
    for k, tabellina in enumerate(l):#enumerate numera le liste ritorna l'indice e l'elemento
        #tabellina è una lista. l è una lista di liste
        print(f"tabellina del {k + 1}: {tabellina}")
        
    f = open("tavolaPitagorica.csv", 'w')
    for k, tabellina in enumerate(l):
        f.write(f"tabellina del {k + 1}: {tabellina}\n")
    f.close()
    
if __name__ == "__main__":
    main()