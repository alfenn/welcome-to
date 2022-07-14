import sys, json, socket

sys.path.append('../../../')
from my_python.Network import Network
from my_python.GenValidMove import GenValidMove
from my_python.OldGameState import OldGameState
from my_python.PlayerState import PlayerState


class RemotePlayerAdapter:
    def __init__(self, in_n: Network, in_p: GenValidMove):
        """
        Initialize remote player adapter
        """
        self.n: Network = in_n
        self.p: GenValidMove = in_p
        # Send json string with name to server after connecting to port
        self.n.send(json.dumps("team5"))

    def play(self):
        while True:
            received: dict = self.n.receive()
            if "game-over" in received:
                self.n.send(json.dumps("ack"))
                return
            # Received { "game-state": ... , "player-state": ... }
            #########
            ## Send a move over the network
            #########
            received_gs = OldGameState(received["game-state"])
            received_ps = PlayerState(inp_ps=received["player-state"])
            generated_move: PlayerState = self.p.generate(received_gs, received_ps)
            self.n.send(str(generated_move))

network_config = json.loads(sys.stdin.read())
# input_str = open('input9_team9.json', 'r').read()
host: str = network_config["host"]
port: int = network_config["port"]
# Initialize remote player adapter with network connectivity and a game-playing
# function
n = Network(host, port)
gvm = GenValidMove()
remote_player: RemotePlayerAdapter = RemotePlayerAdapter(n, gvm)
remote_player.play()

