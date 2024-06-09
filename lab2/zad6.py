import socket

server_address = '212.182.24.27'
port = 2902

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        try:
            number1 = float(input("Podaj  liczbę : "))
        except ValueError:
            if input() == 'exit':
                break
            else:
                print("Niepoprawna liczba")
                continue

        operator = input("Podaj operator (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("Niepoprawny operator.")
            continue

        try:
            number2 = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Niepoprawna liczba ")
            continue

        message = f"{number1} {operator} {number2}"

        sock.sendto(message.encode(), (server_address, port))

        data, server = sock.recvfrom(4096)
        print(f"Otrzymano odpowiedź: {data.decode()}")

finally:
    sock.close()
