import socket

dns_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_server.bind(('127.0.0.1', 3400))

service_registry = {}

print("Servidor DNS está ativo...")

while True:
    data, addr = dns_server.recvfrom(1024)
    request = data.decode().split()
    action = request[0].lower()
    service_name = request[1].lower()

    if action == "register":
        host = request[2]
        port = int(request[3])
        service_registry[service_name] = (host, port)
        print(f"Registrado: {service_name} ({host}:{port})")

    elif action == "unregister":
        if service_name in service_registry:
            del service_registry[service_name]
            print(f"Removido: {service_name}")
        else:
            print(f"Serviço não encontrado: {service_name}")

    elif action == "query":
        if service_name in service_registry:
            host, port = service_registry[service_name]
            response = host
        else:
            response = f"Serviço não encontrado: {service_name}"
        dns_server.sendto(response.encode(), addr)

    else:
        print("Serviço Não Encontrado!")