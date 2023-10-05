import socket

SERVER = "192.168.0.100"
PORT = 12345

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER, PORT))

while True:
    print("Exemplo de operação : 4 + 5")

    inp = input()
    if inp == "Sair":
        break

    client.send(inp.encode())
 
    resposta = client.recv(1024)
    print("O resultado é  "+resposta.decode())
    print("Digite sair para finalizar")
 
client.close()