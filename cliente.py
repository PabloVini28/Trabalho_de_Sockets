import socket

server_ip = 'IP DO SERVIDOR'
port = 12345

socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_cliente.connect((server_ip,port))

print("Conexão bem sucedida")
print("Digite 'sair' para encerrar!")

while True:

    lado_1 = input("Informe a largura em metros: ")

    if lado_1.lower() == 'sair':
        print("Saída confirmada!")
        break

    lado_2 = input("Informe o comprimento em metros: ")

    if lado_2.lower() == 'sair':
        print("Saída confirmada!")
        break

    socket_cliente.send(str(lado_1).encode())
    socket_cliente.send(str(lado_2).encode())

    resultado = socket_cliente.recv(1024).decode()

    print(resultado)

socket_cliente.close()