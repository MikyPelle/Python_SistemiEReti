import math
def trova_n_narc(n):
    narc = False
    centinaia = n // 100
    decine = (n % 100) // 10
    unita = n % 10
    c = math.pow(unita, 3) + math.pow(decine, 2) + math.pow(centinaia, 3)
    if c == n:
        narc = True
    return narc

def main():
    n_narc = []
    for n in range(1, 1000):
        if trova_n_narc(n) ==  True:
            n_narc.append(n)
    print(n_narc)
            


if __name__ == "__main__":
    main()