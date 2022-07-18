import socket, json, threading
HEADER = 8192
class Network:
    def __init__(self, host: str, port: int):
        """
        Networking code that manages connection with server
        """
        self.host: str = host
        self.port: int = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

    def send(self, payload: str):
        """
        Function that sends bytes over the network to the configured server
        """
        self.s.send(payload.encode())
        self.s.send("\n".encode())

    def receive(self):
        """
        Listens from the network connection and returns a decoded python
        representation of the data structure sent from the server
        """
        return json.loads(self.s.recv(HEADER).decode())

class MyServer:
    def __init__(self, players: int, port: int):
        """
        Networking code that manages connections with clients
        """
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((socket.gethostbyname(socket.gethostname()), self.port))
        self.players = players

    def handle_client(self, connection, address):
        """
        Function that receives a message, padded with a header (to determine the length of the next message)
        and closes the connection with the client if we reach a "game-over" state
        """
        connected = True
        while connected:
            msg_length = connection.recv(HEADER).decode('utf-8')
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode('utf-8')
            if msg == "ack":
                connected = False

        connection.close()

    def start(self):
        """
        Function to begin listening and to start the server
        """
        self.server.listen()
        # print("started")
        if self.server.recv(HEADER).decode() == "started":
            while True:
                connection, address = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(connection, address))
                thread.start()
