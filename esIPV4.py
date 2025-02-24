import ipaddress

def main():
    ipV4 = input("Inserisci un indirizzo IPV4: ")
    sub = input("Inserisci la subnet-mask(/n): ")
    
    ipv4pieno = ipV4 + sub
    ip =ipaddress.IPv4Address(ipV4)
    
    if ip.is_private == True:
        print(f"L'indirizzo {ip} è privato.")
    else:
        print(f"L'indirizzo {ip} non è pubblico.")
    
    if ip.is_loopback == True:
        print(f"L'indirizzo {ip} è loopback.")
    else:
        print(f"L'indirizzo {ip} non è loopback.")
        
    ipRete = ipaddress.IPv4Network(ipv4pieno, strict=False)
    if ipv4pieno == str(ipRete):
        print(f"L'indirizzo {ip} è network.")
        
    else:
        print(f"L'indirizzo {ip} non è network.")
    print(f"indirizzo di rete {ipRete}")
    hosts = list(ipRete.hosts())
    print(f"il primo host è --> {hosts[0]}")
    print(f"l'ultimo host è --> {hosts[-1]}")

    
    
if __name__ == "__main__":
    main()