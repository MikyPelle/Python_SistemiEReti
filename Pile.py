def push(pila, elemento):
    pila.append(elemento)
    
def pop(pila):
    x = pila.pop()
    return x

def main():
    pila = [1, 2, 3, 4]
    push(pila, 10)
    print(pila)
    x = pop(pila)
    print(x, pila)
    """pila.append(5) #push
    print(pila)
    x = pila.pop()
    print(x)
    print(pila)"""
    
if __name__ == "__main__":
    main()