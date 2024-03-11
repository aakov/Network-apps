import socket

def pobierz_hostname(adres_ip):
    try:
        hostname = socket.gethostbyaddr(adres_ip)
        print(hostname[0])
    except socket.herror:
        print(f"Nie można znaleźć nazwy hosta ")

adres_ip = input("Podaj adres IP: ")
pobierz_hostname(adres_ip)