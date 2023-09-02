import socket
import threading
import signal
import sys

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 12346))

dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_udp_client.sendto(b"register servidorUDP localhost 12346", ('localhost', 53))

print("Servidor UDP da Calculadora Remota está ativo... (Caso queira encerrar o servidor, aperte 'Ctrl + C')")

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Erro: " + str(e)

def exit_handler(sig, frame):
    print("Encerrando servidor UDP...")
    dns_udp_client.sendto(b"unregister servidorUDP", ('localhost', 53))
    udp_server.close()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

def server_thread():
    while True:
        udp_data, udp_addr = udp_server.recvfrom(1024)
        print(f"Mensagem UDP de {udp_addr}: {udp_data.decode()}")
        
        response = calculate(udp_data.decode())
        
        udp_server.sendto(response.encode(), udp_addr)

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
