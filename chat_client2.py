#client
import socket
from threading import Thread
import csv

SERVER_ADDRESS = ("192.168.1.127", 8000)
BUFFER_SIZE = 4096
NICKNAME = "Pelle"
MY_ADDRESS = ("192.168.1.122", 8000)

class MioThread(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s

    def run(self):
        #codice del thread
        while True:
            data, sender_address = self.s.recvfrom(BUFFER_SIZE)
            nome_mit = cercaMittente(sender_address)
            print(f"Ricevuto {data.decode()}; da: {nome_mit}")

def miPresento(s):
    stringa = f"§presentazione" + "$" + NICKNAME
    s.sendto(stringa.encode(), SERVER_ADDRESS) #per trasmettere stringhe binarie

def cercaMittente(address):
    nome = None
    with open("Rubrica.csv", "r", newline='') as f: 
        csv_reader = csv.reader(f, delimiter=',')
        for riga in csv_reader:
                if riga[1] == address[0] and riga[2] == str(address[1]):
                    nome = riga[0]
    return nome

def main():
    ready = True
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    t = MioThread(s)
    miPresento(s)
    t.start()
    while True:
        string = input("-> ")
        dest = ""
        if string != "list":
            dest = input("inserire nick del destinatario: ")
        packet = f"{string}|{NICKNAME}|{dest}"
        s.sendto(packet.encode(), SERVER_ADDRESS) #per trasmettere stringhe binarie
        if ready:
            ready = False

if __name__ == "__main__":
    main()