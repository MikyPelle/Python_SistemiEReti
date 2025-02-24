def tronca(lista):
    del lista[0]
    del lista[-1]
    return None

def main():
    l = [1, 2, 3, 4]
    tronca(l)
    print(l)  

if __name__ == "__main__":
    main()
