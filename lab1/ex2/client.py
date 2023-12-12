import socket
import threading

class ChatClient:
    def __init__(self):
        self.HOST = socket.gethostname()
        self.PORT = 5050
        self.FORMAT = 'utf-8'
        self.nickname = input("Write your nickname: ")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode(self.FORMAT)
                if message == 'NICK':
                    self.client.send(self.nickname.encode(self.FORMAT))
                else:
                    print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f'{self.nickname}: {input()}'
            self.client.send(message.encode(self.FORMAT))

chat_client = ChatClient()

receive_thread = threading.Thread(target=chat_client.receive)
receive_thread.start()

write_thread = threading.Thread(target=chat_client.write)
write_thread.start()
