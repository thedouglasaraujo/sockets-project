import socket
import time

def tcp_client(expression):
    host = '127.0.0.1'
    port = 12345

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
