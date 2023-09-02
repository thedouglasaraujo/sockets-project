import socket
import time

def udp_client(expressions):
    host = '127.0.0.1'
    port = 12346

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

udp_client(equations)

input("\nPressione Enter para encerrar o programa...")
