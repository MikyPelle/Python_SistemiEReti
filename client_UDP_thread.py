import socket
from threading import Thread

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096 #byte

class MyThread(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.running = True

    def run(self): 
        while self.running:
            data, sender_address = self.s.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"Server: {string}")
    def kill(self):
        self.running = False
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    t = MyThread(s)
    pronto = True
    while True:
        string = input("-> ")
        binary_string = string.encode()
        s.sendto(binary_string, SERVER_ADDRESS)
        if pronto:
            t.start()
            pronto = False
    
if __name__ == "__main__":
    main()