import socket
import threading
import signal
import sys

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(('localhost', 12345))
tcp_server.listen(5)

dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_udp_client.sendto(b"register servidorTCP localhost 12345", ('localhost', 53))

print("Servidor TCP da Calculadora Remota está ativo... (Caso queira encerrar o servidor, aperte 'Ctrl + C')")

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Erro: " + str(e)

def exit_handler(sig, frame):
    print("Encerrando servidor TCP...")
    dns_udp_client.sendto(b"unregister servidorTCP", ('localhost', 53))
    tcp_server.close()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

def server_thread():
    while True:
        tcp_conn, tcp_addr = tcp_server.accept()
        print(f"Conexão TCP de {tcp_addr}")
        data = tcp_conn.recv(1024).decode()
        
        response = calculate(data)
        
        tcp_conn.send(response.encode())
        tcp_conn.close()

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
