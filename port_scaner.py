# port_scanner.py
import socket

def scan_ports(target):
    print(f"\n[*] Target: {target}")
    print("[*] Scanning common ports (1-100)...\n")

    for port in range(1, 101):  # Common first 100 ports
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except socket.error:
            print(f"[!] Couldn't connect to {target}")
            break

if __name__ == "__main__":
    target_ip = input("Enter IP address or domain name: ")
    scan_ports(target_ip)
