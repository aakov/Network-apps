import socket

def pobierz_adres_ip(hostname):
    try:
        adres_ip = socket.gethostbyname(hostname)
        print(adres_ip)
    except socket.gaierror:
        print(f"Nie można znaleźć adresu IP dla hosta {hostname}")

hostname = input("Podaj nazwę hosta: ")
pobierz_adres_ip(hostname)