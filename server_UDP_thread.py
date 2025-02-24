import socket
from threading import Thread

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096 #byte

class MyThread(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.running = True
        self.senderAddress = None
    def run(self): 
        while self.running:
            data, self.senderAddress = self.s.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"Client: {string}")
    def kill(self):
        self.running = False
    
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    t = MyThread(s)
    t.start()
    while True:
        if t.senderAddress != None:
            string = input("-> ")
            bynary = string.encode()
            s.sendto(bynary, t.senderAddress)  
    
if __name__ == "__main__":
    main()