import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        string = input("> ")
        s.sendall(string.encode())
        message = s.recv(BUFFER_SIZE)
        print(message.decode())
        if (message.decode() == "HAI VINTO") or (message.decode() == "HAI PERSO"):
            break
    s.close()

if __name__ == '__main__':
    main()