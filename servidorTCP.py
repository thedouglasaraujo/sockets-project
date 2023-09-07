import socket
import threading
import signal
import sys

def server_thread():
    while True:
        tcp_conn, tcp_addr = tcp_server.accept()
        print(f"Conexão TCP de {tcp_addr}")
        data = tcp_conn.recv(1024).decode()
        
        response = calculate(data)
        
        tcp_conn.send(response.encode())
        tcp_conn.close()

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Erro: " + str(e)
    
def exit_handler(sig, frame):
    print("Encerrando servidor TCP...")
    dns_udp_client.sendto(b"unregister servidorTCP", ('127.0.0.1', 3400))
    tcp_server.close()
    sys.exit(0)

dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_udp_client.sendto(b"register servidorTCP 127.0.0.1 12345", ('127.0.0.1', 3400))
dns_udp_client.close()

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 12345))
tcp_server.listen(5)

print("Servidor TCP da Calculadora Remota está ativo... (Caso queira encerrar o servidor, aperte 'Ctrl + C')")

signal.signal(signal.SIGINT, exit_handler)

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass