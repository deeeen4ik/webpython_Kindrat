import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
print(f"Connecting to the server {SERVER_ADDRESS}:{SERVER_PORT}")

while True:
    message = input("Enter the text to send to the server (to exit, enter 'exit'): ")

    client_socket.sendall(message.encode('utf-8'))

    if message.lower() == 'exit':
        break

client_socket.close()
