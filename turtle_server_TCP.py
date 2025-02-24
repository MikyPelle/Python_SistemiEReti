import socket
import threading
import time
import turtle
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
comandi = ["w","W","d","D","s","S","a","A"]

class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
        self.sciolla = turtle.Turtle()
    def run(self):
        while self.running:
            message = self.connection.recv(BUFFER_SIZE)#bloccante
            command = message.decode()
            if command != "EXIT":
                self.disegnaLista(command)
            else:
                self.kill()    
            
    def disegnaLista(self,command):
        if command == "w" or command =="W":
            self.sciolla.forward(100)
        elif command == "d" or command == "D":
            self.sciolla.right(90)
        elif command == "a" or command == "A":
            self.sciolla.left(90)
        elif command == "s" or command == "S":
            self.sciolla.backward(100)
        else: 
            print("comando errato")
    def kill(self):
        self.running = False
        self.connection.close()
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    finestra = turtle.Screen()
    while True:
        connection, client_address = s.accept()#bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()
        finestra.mainloop()
    s.close()

if __name__ == '__main__':
    main()