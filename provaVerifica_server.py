#Progettare in python 3:
#   -un server TCP che quando viene eseguito sorteggia un numero intero casuale
#    tra 1 e 100
#   -al server si connettono almeno due client
#   -gli utenti tramite i client inviano al server un numero tentando di indovinare 
#    il numero casuale scelto dal server
#   -il server risponde ai client nei modi seguenti:
#    *"HAI VINTO" se il client ha indovinato il numero
#    *"TROPPO BASSO" se il numero del client è <
#    *"TROPPO ALTO" se il numero del client è >
#   -quando un client vince agli altri client viene inviato "HAI PERSO"

import socket
import threading
import random
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
num_rand = random.randint(1,100)
blocco = threading.Lock()
vincitore = False

class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
    def run(self):
        global vincitore
        while self.running:
            data = self.connection.recv(BUFFER_SIZE)
            numero = int(data.decode())
            with blocco:
                if not vincitore:
                    if numero < num_rand:
                        self.connection.sendall("TROPPO BASSO".encode())
                    elif numero > num_rand:
                        self.connection.sendall("TROPPO ALTO".encode())
                    else:
                        self.connection.sendall("HAI VINTO".encode())
                        vincitore = True
                        self.kill()
                else:
                    self.connection.sendall("HAI PERSO".encode())
                    self.kill()

    def kill(self):
        self.running = False
        self.connection.close()
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address = s.accept()#bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()
    s.close()

if __name__ == '__main__':
    main()