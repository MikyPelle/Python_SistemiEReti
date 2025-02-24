#creare un server TCP che permette la connessione a un client alla volta e mette in coda gli altri
#il client rimane connesso per 30 secondi circa
#il client manda la richiesta con il nome e il server controlla che non sia già connesso
import socket
import threading
import time
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

lista_prenotazioni = []

class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
    def run(self):
        global lista_prenotazioni
        message = self.connection.recv(BUFFER_SIZE)#bloccante
        nome = message.decode()
        if nome in lista_prenotazioni:
            self.connection.sendall(f"{message.decode()} già prenotato".encode())
        else:
            lista_prenotazioni.append(nome)
            self.connection.sendall(f"{message.decode()} si è prenotato per {len(lista_prenotazioni)}".encode())
        print(lista_prenotazioni)
        while self.running:
            if nome in lista_prenotazioni:
                pass
            else:
                self.connection.sendall(f"sei stato rimosso dalla coda".encode())
                self.kill()
    def kill(self):
        self.running = False
        self.connection.close()
    def kill(self):
        self.running = False
        self.connection.close()
class Remove_client(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True
    def run(self):
        global lista_prenotazioni
        while self.running:
            if len(lista_prenotazioni) != 0:
                time.sleep(10)
                lista_prenotazioni.remove(lista_prenotazioni[0])
                print(lista_prenotazioni)
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    remove_client = Remove_client()
    remove_client.start()
    while True:
        connection, client_address = s.accept()#bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()
        print(lista_prenotazioni)
    s.close()

if __name__ == '__main__':
    main()