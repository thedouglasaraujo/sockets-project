import socket
import time

def consultar_dns(server):
    client_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_dns.sendto(server.encode(), ('127.0.0.1', 3400))
    response, address = client_dns.recvfrom(1024)
    client_dns.close()
    return response.decode()

def udp_client(expressions):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for expression in expressions:
        expression_str = expression[0]

        start_time = time.perf_counter()

        client_socket.sendto(expression_str.encode(), (host, port))
        result, _ = client_socket.recvfrom(1024)

        end_time = time.perf_counter()

        print("Expressão:", expression_str)
        print("Resultado:", result.decode())

        elapsed_time = end_time - start_time
        elapsed_time_ms = elapsed_time * 1000
        print("Tempo total:", elapsed_time_ms, "milissegundos")
        print("-" * 30)

    client_socket.close()

equations = [
    ["2 + 3"],
    ["10 - 5"],
    ["6 * 4"],
    ["15 / 3"],
    ["2 ** 4"],
    ["20 + 8"]
]

host = consultar_dns("query servidorUDP")
port = 12346

try:
    udp_client(equations)
except:
    dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns_udp_client.sendto(b"unsuccessful_connection servidorudp", ('127.0.0.1', 3400))
    exit()

input("\nPressione Enter para encerrar o programa...")