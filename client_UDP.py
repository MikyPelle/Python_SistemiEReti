import socket

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096 #byte

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    string = input("-> ")
    binary_string = string.encode()
    s.sendto(binary_string, SERVER_ADDRESS)
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    string = data.decode()
    print(f"ricevuto {string} da {sender_address}")
    if string == "EXIT":
        break