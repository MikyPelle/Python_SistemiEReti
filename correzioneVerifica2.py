def main():
    for numero in range(1,1000): 
        if sum([int(cifra)**3 for cifra in str(numero)]) == numero:
            print(f"il numero {numero} è narcisista")        
    
if __name__ == "__main__":
    main()