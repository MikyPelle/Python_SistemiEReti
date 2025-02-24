def main():
    x = [0, 1, 2, 3, 5, 6, 7, 8]
    lung = len(x)
    mezzo = lung // 2
    y = x[:mezzo]
    z = x[mezzo:]
    
    y.append(z[0])
    print(f"Lista intera --> {x}")
    print(f"Prima metà della lista --> {y}")
    print(f"Seconda metà della lista --> {z}")

if __name__ == "__main__":
    main()