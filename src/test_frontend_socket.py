import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"yes this is test data that the server is pinging back!")
    data = s.recv(1024)

print(f"Received {data!r}")

