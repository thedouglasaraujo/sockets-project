class NameServer:
    def __init__(self):
        self.registry = {}

    def register(self, name, address):
        self.registry[name] = address

    def lookup(self, name):
        return self.registry.get(name, "Serviço não encontrado")

if __name__ == "__main__":
    name_server = NameServer()

    name_server.register("tcp_calculator", ("127.0.0.1", 12345))
    name_server.register("udp_calculator", ("127.0.0.1", 12346))

    while True:
        query = input("Digite o nome do serviço para consulta: ")
        address = name_server.lookup(query)
        print("Endereço do serviço:", address)
