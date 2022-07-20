import json
from my_python.Network import Network
from my_python.GenValidMove import GenValidMove
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState


class PlayerAdapter:
    def __init__(self):
        self.game_over = False

    def play(self):
        pass

class RemotePlayerAdapter(PlayerAdapter):
    def __init__(self, in_n: Network, in_p: GenValidMove):
        """
        Initialize remote player adapter
        """
        super().__init__()
        self.n: Network = in_n
        self.p: GenValidMove = in_p
        # Send json string with name to server after connecting to port
        self.n.send(json.dumps("team5"))

    def play(self):
        while True:
            received: dict = self.n.receive()
            if "game-over" in received:
                self.n.send(json.dumps("ack"))
                self.game_over = True
                return
            # Received { "game-state": ... , "player-state": ... }
            #########
            ## Send a move over the network
            #########
            received_gs = GameState(received["game-state"])
            received_ps = PlayerState(inp_ps=received["player-state"])
            generated_move: PlayerState = self.p.generate(received_gs, received_ps)
            self.n.send(str(generated_move))
