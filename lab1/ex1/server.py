import socket
import datetime

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

server_socket.listen(1)
print(f"The server is listening on {SERVER_ADDRESS}:{SERVER_PORT}")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    data = client_socket.recv(1024).decode('utf-8')

    if not data:
        break

    print(f"Recived: '{data}'")
    print("Reply sent...")
    import time
    time.sleep(5)
    if len(data.encode('utf-8')) == client_socket.sendall(data.encode('utf-8')):
        print("All data sent successfully")

client_socket.close()
server_socket.close()
