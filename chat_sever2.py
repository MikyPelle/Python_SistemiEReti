#server
import socket 
import csv

MY_ADDRESS = ("127.0.0.1", 9000) #con 0.0.0.0 python prende indirizzo della macchina
BUFFER_SIZE = 4096 

def salvaSuRubrica(nick_sender, porta, ip):

    with open("Rubrica.csv", "a", newline='') as f: 
        writer = csv.writer(f)
        writer.writerow([nick_sender, ip, str(porta)])

def cerca_dest(data):
    nick_dest = data.split("|")[2]
    print(nick_dest)
    ip_dest = None
    porta_dest = None
    with open("Rubrica.csv", "r", newline='') as f: 
        csv_reader = csv.reader(f, delimiter=',')
        for riga in csv_reader:
            if riga:
                if (riga[0] == nick_dest):
                    ip_dest = riga[1]
                    porta_dest = int(riga[2])
    return ip_dest, porta_dest
        
def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind(MY_ADDRESS)

    while True:
        data, sender_address = s.recvfrom(BUFFER_SIZE)
        print(f"Messaggio ricevuto da: {sender_address} ({data.decode()})" )
        if data.decode().split("$")[0] == "§presentazione":
            nick_sender = data.decode().split("$")[1]
            porta = sender_address[1]
            ip = sender_address[0]
            salvaSuRubrica(nick_sender, porta, ip)
        elif data.decode() == "$list":
            message = ""
            with open("Rubrica.csv", "r", newline='') as f: 
                csv_reader = csv.reader(f, delimiter=',')
                for riga in csv_reader:
                    pass
                    
        else:
            elementMessage = data.decode().split("|")

            if len(elementMessage) == 3:
                message =  elementMessage[0]
                nick_sender = data.decode().split("|")[1]
                porta = sender_address[1]
                ip = sender_address[0]
                salvaSuRubrica(nick_sender, porta, ip)
                ip_dest, porta_dest = cerca_dest(data.decode())
                if ip_dest != None and porta_dest != None:
                    s.sendto(message.encode(), (ip_dest, porta_dest))
                else:
                    print("il destinatario non è presente in rubrica")
            else:
                print(data.decode())
                print("errore indirizzo ip destinatario")

if __name__ == "__main__":
    main()