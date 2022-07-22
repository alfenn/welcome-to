import json, socket, sys
import threading

sys.path.append('../../../')

from my_python.MoveGeneratorInterface import MoveGeneratorInterface
from my_python.Network import Network
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState
from my_python.validate_move import validate_move
from my_python.exceptions import InvalidPlayerState, InvalidMove, NetworkDisconnect


########################
## Client-side code ####
########################
class PlayerInterface:
    def __init__(self):
        self.name = ''
        self.marked_as_cheater: bool = False
        self.score: int = 0
        self.connected: bool = False
    def receive(self, json_s) -> None:
        """Takes json string representation of the a6 ~request non-terminal, which is either ~{"game-over": ...} or
        ~{"game-state": ~GameState, "player-state": ~PlayerState}.
        Aka. Tells the interface to receive communication from the server."""
        pass
    def send(self) -> str:
        """Returns json string from the player, which is either a network- or a local-player
        Aka. Tells the interface to send communication to the server."""
        pass
    def mark_as_cheater(self) -> None:
        """Called when the server detects cheating and wants to end the game with the player"""
        pass
    def terminate(self) -> None:
        """Terminates connection with either the network- or local-player"""
        pass

# A player that plays over the network
class NetworkPlayer(PlayerInterface):
    def __init__(self, conn: socket.socket):
        super().__init__()
        self.client_connection: socket.socket = conn
        self.connected = True
        full_msg = ''
        while '\n' not in full_msg:
            msg = self.client_connection.recv(8192)
            if len(msg) <= 0: break
            full_msg += msg.decode('utf-8')
        self.name = json.loads(full_msg)    # The first thing a connected network player sends is its name

    def _send_over_network(self, payload: str):
        """Sends bytes over the network from network client"""
        self.client_connection.send(payload.encode())
        self.client_connection.send("\n".encode())

    def receive(self, json_s) -> None:
        # Pass arguments to the client connection
        self._send_over_network(json_s)

    def send(self) -> str:
        full_msg = ''
        while '\n' not in full_msg:
            msg = self.client_connection.recv(8192)
            if len(msg) <= 0: break
            full_msg += msg.decode('utf-8')
        return full_msg
        # return self.client_connection.recv(8192*16).decode()

    def terminate(self) -> None:
        self.client_connection.close()
        self.connected = False

    def mark_as_cheater(self) -> None:
        # Terminate the connection with the network player
        self.marked_as_cheater = True
        self.terminate()


# A player that plays locally
class LocalPlayer(PlayerInterface):
    def __init__(self, mg: MoveGeneratorInterface, name: str):
        super().__init__()
        self.game_is_over: bool = False
        self.move_generator: MoveGeneratorInterface = mg
        self.player_board_state: PlayerState = PlayerState()
        self.name: str = name
        self.connected = True

    def receive(self, json_s) -> None:
        if self.marked_as_cheater:
            raise ValueError(f"Cannot receive() because local player {self.name} has been marked as a cheater")
        deserialized = json.loads(json_s)
        if 'game-over' in deserialized:
            self.game_is_over = True
            return
        elif 'game-state' in deserialized and 'player-state' in deserialized:
            gs = GameState(deserialized["game-state"])
            ps = PlayerState(inp_ps=deserialized["player-state"])
            self.player_board_state = self.move_generator.generate(gs, ps)
            return
        raise ValueError("Passed invalid arguments to LocalPlayer.receive()")

    def send(self) -> str:
        """Returns either json string "ack" or the player-board-state as a ~PlayerState"""
        if self.marked_as_cheater:
            raise ValueError(f"Cannot send() because local player {self.name} has been marked as a cheater")
        if self.game_is_over:
            return json.dumps('ack')
        else:
            return json.dumps(self.player_board_state.return_literal())

    def terminate(self) -> None:
        # Doesn't really do anything, just updates the class attribute
        self.connected = False

    def mark_as_cheater(self) -> None:
        self.marked_as_cheater = True
        self.terminate()


# Takes in any playing function and plays a game over the network with it
class RemotePlayerAdapter:
    def __init__(self, mg: MoveGeneratorInterface, host: str, port: int):
        self.player = LocalPlayer(mg, 'team5')
        self.network = Network(host, port)
        self.network.send(json.dumps(self.player.name))

    def play(self):
        ## The game playing loop...
        while True:
            request: str = self.network.receive()           # store the json string a6 ~request non-terminal from the network server
            self.player.receive(request)                    # pass the json serialized ~request to the local player
            response = self.player.send()                   # store the decoded python a6 ~response non-terminal from the local player
            self.network.send(response)         # send a json string representation of the local player's response to the request
            # Keep playing until the local player decides to end the game
            if response == "ack":
                break





#########################
## Server-side code #####
#########################

def play_game(p: PlayerInterface, results: list, results_id: int, lock: threading.Lock) -> None:
    """Plays a game with an inputted player. Doesn't care if the player it gets plays over the network or if it's a
    local player."""
    # with lock:
    #     print(f"Starting thread {results_id}", file=sys.stderr)
    curr_game_state = GameState()
    curr_player_state = PlayerState()
    new_player_state = PlayerState()
    with lock:
        results[results_id] = [p, PlayerState()]
    while True:
        p.receive(json.dumps({"game-state": curr_game_state.return_literal(), "player-state": new_player_state.return_literal()}))
        ### Get the result from the player and check if it's a cheater
        response: str = p.send()
        try:
            ## Cheating case 1: invalid json
            response = json.loads(response)
            new_player_state = PlayerState(inp_ps=response)
            ## Cheating case 2: invalid move
            # print(f'ps1: {curr_player_state}\nps2: {new_player_state}', file=sys.stderr)
            validate_move(gs=curr_game_state, ps1=curr_player_state, ps2=new_player_state)
            ## Cheating case 3: connection terminated
            #   - https://stackoverflow.com/questions/43178999/how-to-know-that-clients-disconnects-server-in-socket

            if response == b'':
                raise NetworkDisconnect("Player disconnected from the server")
        except (json.decoder.JSONDecodeError, InvalidPlayerState, InvalidMove, NetworkDisconnect) as e:
            p.mark_as_cheater()
            # with lock:
                # print(f"Stopping thread {results_id}. Detected cheater.", file=sys.stderr)
            return
        ### If it's not a cheater, check if it's the end of the game.
        #   Game ends if:
        #       1. player crosses off their third refusal
        #       2. player achieves all 3 city plans
        #       3. player has built all the houses on the street
        if new_player_state.refusals == 3 \
                or "blank" not in new_player_state.city_plan_score \
                or new_player_state.no_space():
            with lock:
                results[results_id][1] = new_player_state
                # print(f"Stopping thread {results_id}. Stored final playerstate.", file=sys.stderr)
            return

        # If it's not the end of the game, generate a game state for the player and send it the game state together with its
        #   current-board-state.
        # we're not generating a new game state, just recycling the same one
        # This is totally wrong: we need to at least update it with city-plans that were claimed
        curr_player_state = new_player_state
