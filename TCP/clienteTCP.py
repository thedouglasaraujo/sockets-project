import socket
import time

def consultar_dns(server):
    client_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_dns.sendto(server.encode(), ('127.0.0.1', 3400))
    response, address = client_dns.recvfrom(1024)
    client_dns.close()
    return response.decode()

def tcp_client(expression):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    expression_str = expression[0]

    start_time = time.perf_counter()

    client_socket.send(expression_str.encode())
    result = client_socket.recv(1024).decode()

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    elapsed_times_tcp.append(elapsed_time_ms)

    with open('temposTCP.txt', 'a') as file:
        file.write(f"Expressão: {expression_str}\n")
        file.write(f"Tempo: {elapsed_time_ms} milissegundos\n")
        file.write("-" * 30 + "\n")

    print("Expressão:", expression_str)
    print("Resultado:", result)
    print("Tempo:", elapsed_time_ms, "milissegundos")
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

consulta = consultar_dns("query servidorTCP").split(":")
host = consulta[0]
port = int(consulta[1])

elapsed_times_tcp = []
with open('temposTCP.txt', 'w') as file:
    file.write(f"Armazenando tempo total de execução TCP\n")
    file.write("-" * 30 + "\n")

for equation in equations:
    try:
        tcp_client(equation)
    except:
        dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_udp_client.sendto(b"unsuccessful_connection servidortcp", ('127.0.0.1', 3400))
        exit()

total_time_tcp = sum(elapsed_times_tcp)

with open('temposTCP.txt', 'a') as file:
    file.write(f"Tempo total TCP: {total_time_tcp} milissegundos\n")

input("\nPressione Enter para encerrar o programa...")
