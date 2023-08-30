import socket
import time

def register_with_name_server(service_name, address):
    name_server_host = '127.0.0.1'
    name_server_port = 12347

    name_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    name_socket.sendto(f"REGISTER {service_name} {address[0]} {address[1]}".encode(), (name_server_host, name_server_port))
    name_socket.close()

def tcp_client(expression):
    host = '127.0.0.1'
    port = 12345

    register_with_name_server("tcp_calculator", (host, port))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    start_time = time.perf_counter()

    client_socket.send(expression.encode())
    result = client_socket.recv(1024).decode()

    end_time = time.perf_counter()

    print("Resultado:", result)

    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000
    print("Tempo total:", elapsed_time_ms, "milissegundos")

    client_socket.close()

if __name__ == "__main__":
    expression = "10 + 5"
    tcp_client(expression)
