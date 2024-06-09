import socket

server_address = '127.0.0.1'
server_port = 2900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))


try:
    while True:
        data, address = server_socket.recvfrom(4096)
        message = data.decode('utf-8')
        print(f"Odebrano wiadomość: {message} od {address}")

        try:
            number1, operator, number2 = message.split()
            number1 = float(number1)
            number2 = float(number2)

            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2
            elif operator == '*':
                result = number1 * number2
            elif operator == '/':
                result = number1 / number2
            else:
                raise ValueError("Nieznany operator")

            server_socket.sendto(str(result).encode('utf-8'), address)
        except Exception as e:
            error_message = "BAD SYNTAX"
            server_socket.sendto(error_message.encode('utf-8'), address)
finally:
    server_socket.close()
