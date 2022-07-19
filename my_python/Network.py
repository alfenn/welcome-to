import socket, json, threading

from my_python.validate_move import validate_move
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState

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
        def __init__(self, players: list, port: int):
            """
            Networking code that manages connections with clients
            """
            # self.port = port
            self.port = 8103
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
                # send a gamestate and playerstate over and receive a move in response
                msg_length = connection.recv(HEADER).decode('utf-8')
                msg_length = int(msg_length)
                msg = json.loads(connection.recv(msg_length).decode('utf-8'))
                # client closing protocol - "ack" signifies game-over
                if msg == "ack": break
                # if the player has cheated, close the client and produce "false" for returning score
                received_ps: PlayerState(inp_ps=msg["player-state"])

            connection.close()

        def start(self):
            """
            Function to begin listening and to start the server
            """
            self.server.listen()
            print("started")
            while True:
                connection, address = self.server.accept()
                raise ValueError("connected!")
                print(f"Connection to {connection}, {address} successful")
                thread = threading.Thread(target=self.handle_client, args=(connection, address))
                thread.start()
                print(f"There are currently {threading.active_count()-1} active threads")