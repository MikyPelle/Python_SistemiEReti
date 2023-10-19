def main():
    x = 5
    y = 20
    
    print(f"x = {x} y = {y}")
    
    x, y = y, x
    
    print(f"x = {x} y = {y}")

if __name__ == "__main__":
    main()