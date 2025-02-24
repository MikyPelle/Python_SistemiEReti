def main():
    rubrica = {}
    f = open("Rubrica.txt", "r")
    righe = f.readline()
    f.close()
    
    for riga in righe:
        #restituisce i campi
        campi = riga.split(", ")
        #sostituisco il carttere
        numeroTelefonico = int(campi[1].replace("\n", ""))
        nome = campi[0]
        rubrica[numeroTelefonico] = nome
        
    
if __name__ == "__main__":
    main()