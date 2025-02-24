import math
def mia_radq(a):
    epsilon = 0.00000001
    x = a
    while True:
        #print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
        
    return y

def test_radq():
    print(f"{'a':<10} {'mia_radq(a)':<20} {'math.sqrt(a)':<20} {'diff':<20}") #il comando :<(numero) permette di spaziare il testo del numero di spazi desiderati
    print(f"{'-':<10} {'-----------':<20} {'-----------':<20} {'-----------':<20}")
    for a in range(1,10):
        print(f"{a:<10} {mia_radq(a):<20} {math.sqrt(a):<20} {abs(mia_radq(a)-math.sqrt(a)):<20}")

def main():
    test_radq()


if __name__ == '__main__':
    main()