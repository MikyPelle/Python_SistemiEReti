def main():
    x = [0, 1, 2, 3, 5, 6, 7, 8]
    y = []
    z = []
    
    for i in x:
        if i < len(x) / 2:
            y.append(i)
        else:
            z.append(i)
            
    print(x)
    print(y)
    print(z)
    y.append(5)
    print(y)


if __name__ == "__main__":
    main()