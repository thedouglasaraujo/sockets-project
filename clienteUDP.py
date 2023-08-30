import socket
import time

def register_with_name_server(service_name, address):
    name_server_host = '127.0.0.1'
    name_server_port = 12347

    name_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    name_socket.sendto(f"REGISTER {service_name} {address[0]} {address[1]}".encode(), (name_server_host, name_server_port))
    name_socket.close()

def udp_client(expression):
    host = '127.0.0.1'
    port = 12346

    register_with_name_server("udp_calculator", (host, port))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    start_time = time.perf_counter()

    client_socket.sendto(expression.encode(), (host, port))
    result, _ = client_socket.recvfrom(1024)

    end_time = time.perf_counter()

    print("Resultado:", result.decode())

    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print("Tempo total:", elapsed_time_ms, "milissegundos")

if __name__ == "__main__":
    expression = "20 - 8"
    udp_client(expression)
