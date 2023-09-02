import socket
import time

def tcp_client(expression):
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    expression_str = expression[0]

    start_time = time.perf_counter()

    client_socket.send(expression_str.encode())
    result = client_socket.recv(1024).decode()

    end_time = time.perf_counter()

    print("Expressão:", expression_str)
    print("Resultado:", result)

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

for equation in equations:
    try:
        tcp_client(equation)
    except:
        dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_udp_client.sendto(b"unsuccessful_connection meu_servico", ('localhost', 53))
        exit()

input("\nPressione Enter para encerrar o programa...")
