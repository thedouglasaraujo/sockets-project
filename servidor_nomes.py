import socket
import signal
import sys

class NameServer:
    def __init__(self):
        self.registry = {}

    def register(self, name, address):
        self.registry[name] = address

    def unregister(self, name):
        if name in self.registry:
            del self.registry[name]

    def lookup(self, name):
        return self.registry.get(name, "Serviço não encontrado")

def handle_shutdown(signum, frame):
    print("\nEncerrando servidor de nomes...")
    sys.exit(0)

def name_server():
    host = '127.0.0.1'
    port = 12347

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    name_server = NameServer()

    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    print("Servidor de Nomes aguardando conexões...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        data = data.decode()

        if data.startswith("REGISTER"):
            _, service_name, service_host, service_port = data.split()
            service_address = (service_host, int(service_port))
            name_server.register(service_name, service_address)
            print(f"Registrado serviço '{service_name}' em {service_address}")
        elif data.startswith("UNREGISTER"):
            _, service_name = data.split()
            name_server.unregister(service_name)
            print(f"Removido serviço '{service_name}'")
        else:
            response = name_server.lookup(data)
            server_socket.sendto(response.encode(), addr)

name_server()
