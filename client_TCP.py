import socket
SERVER_ADDRESS = ("192.168.1.122", 9090)
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    string = input("> ")
    s.sendall(string.encode())
    message = s.recv(BUFFER_SIZE)#bloccante
    print(f"ricevuto <{message.decode()}> dal server")
    s.close()

if __name__ == '__main__':
    main()