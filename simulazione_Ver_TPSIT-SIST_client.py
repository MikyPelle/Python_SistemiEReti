import socket
import time
SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    string = input("inserisci il nome\n> ")
    s.sendall(string.encode())
    message = s.recv(BUFFER_SIZE)#bloccante
    print(message.decode() + "°")
    message = s.recv(BUFFER_SIZE)#bloccante
    print(message.decode())
    s.close()


if __name__ == '__main__':
    main()