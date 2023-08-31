import socket

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Erro ao calcular"

def tcp_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Servidor TCP aguardando conexões...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")

        data = conn.recv(1024).decode()
        print(f"Expressão recebida: {data}")

        result = calculate(data)
        conn.send(result.encode())

        conn.close()

tcp_server()
