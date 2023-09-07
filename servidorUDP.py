import socket
import threading
import signal
import sys

def server_thread():
    while True:
        udp_data, udp_addr = udp_server.recvfrom(1024)
        print(f"Mensagem UDP de {udp_addr}: {udp_data.decode()}")
        
        response = calculate(udp_data.decode())
        
        udp_server.sendto(response.encode(), udp_addr)

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Erro: " + str(e)
    
def exit_handler(sig, frame):
    print("Encerrando servidor UDP...")
    dns_udp_client.sendto(b"unregister servidorUDP", ('127.0.0.1', 3400))
    udp_server.close()
    dns_udp_client.close()
    sys.exit(0)
    
dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_udp_client.sendto(b"register servidorUDP 127.0.0.1 12346", ('127.0.0.1', 3400))

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('127.0.0.1', 12346))

print("Servidor UDP da Calculadora Remota está ativo... (Caso queira encerrar o servidor, aperte 'Ctrl + C')")

signal.signal(signal.SIGINT, exit_handler)

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass