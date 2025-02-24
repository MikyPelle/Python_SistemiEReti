def niente_e(word):
    if 'e' not in word:
        return True
    else:
        return False
def main():
    word = "come"
    if niente_e(word):
        print("la parola non contiene 'e' ")
    else:
        print("la parola contiene 'e'")
if __name__ == '__main__':
    main()