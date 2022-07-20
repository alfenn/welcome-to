import socket, json, threading

from my_python.validate_move import validate_move
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState

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

