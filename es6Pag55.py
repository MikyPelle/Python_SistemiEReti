def main():
    s = input("Inserisci una parola: ")
    
    for i in range(0,len(s)):
        if i % 2 != 0:
            print(s[i])

def main1():
    s = input("Inserisci una parola: ")
    
    print(s[1::2]) #stampa i caratteri della stringa partendo dal secondo (1) 
                   #fino al foondo (::) saltando 2 caratteri(2)

if __name__ == "__main__":
    main()
    main1()