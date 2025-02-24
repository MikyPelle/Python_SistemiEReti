import socket
import threading
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
    def run(self):
        message = self.connection.recv(BUFFER_SIZE)#bloccante
        print(message.decode())
        self.connection.sendall(message)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address = s.accept()#bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()

if __name__ == '__main__':
    main()