import math

def main():
    #l = [i*i for i in range(int(0, math.sqrt(200)) + 1) if (i*i) % 2 != 0]
    l = [i*i for i in range(0, 1000) if i*i <= 200 and (i*i) % 2 != 0]
    print(l)
    
    
if __name__ == "__main__":
    main()