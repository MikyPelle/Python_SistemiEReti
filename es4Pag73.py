def main():
    cont = 0
    for num in range (1, 201):
        ris = num * num
        if ris <= 200:
            cont += 1

    print(f"I quadrati perfetti sono {cont}")



if __name__ == "__main__":
    main()