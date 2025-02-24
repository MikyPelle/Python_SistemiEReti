def main():
    dizionario = {"nome": "Mario", "cognome": "Rossi"}
    #lista = {"Mario", "Rossi"}
    print(dizionario["nome"])
    
    #aggiunge due elementi nuovi
    dizionario["data nascita"] = "01/01/1900"
    dizionario["età"] = 123
    
    #sovrascrive l'elemento con chiave "nome"
    dizionario["nome"] = "Luca"
    
    print(dizionario)
    
    #ciclo for per dizionario
    for chiave in dizionario:
        #print(dizionario[chiave])
        print(f"Chiave: {chiave} - valore: {dizionario[chiave]}")
        
    rubrica = {38189192: "Mario Rossi",  34875668: "Alice Verdi", 32459973: "Luca Gialli"}
    
    for k,v in dizionario.items(): #cicla sia chiave che elemento in contemporanea
        pass
    
if __name__ == "__main__":
    main()