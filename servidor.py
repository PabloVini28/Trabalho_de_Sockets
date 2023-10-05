import socket

# Configuração do servidor
host = '0.0.0.0'
port = 12345  # Porta em que o servidor estará ouvindo

def calcular_area(lado_a, lado_b):
    return lado_a * lado_b

def determina_tamanho(area):
    if area >= 300:
        return "grande"
    else:
        return "pequeno"

# Cria um objeto de soquete TCP
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o soquete ao endereço e porta especificados
socket_servidor.bind((host, port))

# Coloca o servidor no modo de escuta
socket_servidor.listen(5)

print(f"Servidor TCP aguardando conexão {host}:{port}")
# Aceita conexões dos clientes
socket_cliente, endereco_cliente = socket_servidor.accept()
print(f"Conexão estabelecida com {endereco_cliente}")

while True:
    

    # Recebe os lados do terreno do cliente e calcula a área
    lado_a = float(socket_cliente.recv(1024).decode())
    lado_b = float(socket_cliente.recv(1024).decode())

    area = calcular_area(lado_a, lado_b)
    tamanho = determina_tamanho(area)

    print("Tratamento de nova ocorrência!")
    resposta = f"A área do terreno é {area} metros quadrados e é {tamanho}."
    socket_cliente.send(resposta.encode())

    # Fecha o soquete do cliente após o tratamento da solicitação
    
socket_cliente.close()
# O servidor nunca alcança esta parte enquanto estiver em execução, mas normalmente aqui você fecharia o soquete do servidor após interromper o loop.
# socket_servidor.close()