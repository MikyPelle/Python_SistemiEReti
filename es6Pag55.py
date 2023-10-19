def main():
    s = input("Inserisci una parola: ")
    
    for i in range(0,len(s)):
        if i % 2 != 0:
            print(s[i])

if __name__ == "__main__":
    main()