#server
import socket

MY_ADDRESS = ("0.0.0.0", 9000) 
BUFFER_SIZE = 4096 


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind(MY_ADDRESS)
    while True:
        data, sender_address = s.recvfrom(BUFFER_SIZE)
        print("Messaggio ricevuto da:", sender_address)
        elementMessage = data.decode().split("|")
        if len(elementMessage) == 3:
            message, destinatario_address, porta_destinatario = elementMessage
            try:
                s.sendto(message.encode(), (destinatario_address, int(porta_destinatario)))
                print(f"mando a {destinatario_address} : {porta_destinatario} message: {message} da parte di {sender_address}")
            except:
                print(f"errore causato da {sender_address}")
        else:
            print("errore indirizzo ip destinatario")
            print(data.decode())

if __name__ == "__main__":
    main()