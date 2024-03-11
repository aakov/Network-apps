import ipaddress


adres = input("Podaj adres IP: ")
try:
    ipaddress.IPv4Address(adres)
    print(f"Adres {adres} jest poprawnym adresem")
except ipaddress.AddressValueError:
    try:
        ipaddress.IPv6Address(adres)
        print(f"Adres {adres} jest poprawnym adresem")
    except ipaddress.AddressValueError:
        print(f"Adres {adres} nie jest poprawnym adresem")
