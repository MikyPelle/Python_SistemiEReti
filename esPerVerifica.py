"""chiedere in input un numero dispari e disegnare un rombo con 
degli asterischi in modo che le diagonali abbiano n asterischi"""

def main():
    n = 0
    while n % 2 == 0 and n < 0:
        n = int(input("Inserire un numero intero dispari: "))
        
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
        
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)
    
if __name__ == "__main__":
    main()