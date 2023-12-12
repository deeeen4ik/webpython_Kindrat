import socket
import threading

class ChatServer:
    def __init__(self):
        self.HOST = socket.gethostname()
        self.PORT = 5050
        self.FORMAT = 'utf-8'
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'{nickname} is out!'.encode(self.FORMAT))
                self.nicknames.remove(nickname)
                break

    def start(self):
        while True:
            client, addr = self.server.accept()
            print(f"Connected at the address: {addr}")

            client.send('NICK'.encode(self.FORMAT))
            nickname = client.recv(1024).decode(self.FORMAT)
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f"Your nickname {nickname}")
            self.broadcast(f"{nickname} joined!".encode(self.FORMAT))
            client.send('Joined the server!'.encode(self.FORMAT))

            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

chat_server = ChatServer()
chat_server.start()
