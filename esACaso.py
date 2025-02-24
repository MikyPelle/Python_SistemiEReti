import ipaddress
def mask(network):
    return network.netmask
def main():
    ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    networks = [ipaddress.IPv4Network(ip, strict=False) for ip in ip_address]
    for network in networks:
        print(f"str{mask(network)}")

if __name__ == "__main__":
    main()