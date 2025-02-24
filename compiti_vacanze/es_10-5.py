def ordinata(lista):
    return lista == sorted(lista)

def main():
    print(ordinata([1, 5, 10])) 
    print(ordinata(['b','a','c','e','d']))

if __name__ == "__main__":
    main()
