import socket

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Erro ao calcular"
    
def udp_server():
    host = '127.0.0.1'
    port = 12346

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Servidor UDP aguardando conexões...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Expressão recebida: {data.decode()}")

        result = calculate(data.decode())

        server_socket.sendto(result.encode(), addr)

udp_server()
