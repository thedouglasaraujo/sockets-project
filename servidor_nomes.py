import socket

class NameServer:
    def __init__(self):
        self.registry = {}

    def register(self, name, address):
        self.registry[name] = address

    def lookup(self, name):
        return self.registry.get(name, "Serviço não encontrado")

def name_server():
    host = '127.0.0.1'
    port = 12347

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    name_server = NameServer()

    print("Servidor de Nomes aguardando conexões...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        data = data.decode()

        if data.startswith("REGISTER"):
            _, service_name, service_host, service_port = data.split()
            service_address = (service_host, int(service_port))
            name_server.register(service_name, service_address)
            print(f"Registrado serviço '{service_name}' em {service_address}")
        else:
            response = name_server.lookup(data)
            server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    name_server()
