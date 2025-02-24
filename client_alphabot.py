import socket
SERVER_ADDRESS = ("192.168.1.146", 8000)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        string = input("\ncomandi possibili:\n>avanti: 'F;x'\n>indietro: 'B;x'\n>destra: 'R;x'\n>sinitra: 'L;x'\n>comandi: 'HELP'\n>esci: 'EXIT\n(x = tempo in secondi)\n")
        s.sendall(string.encode())
        message = s.recv(BUFFER_SIZE)
        print(message.decode())
    s.close()

if __name__ == "__main__":
    main()