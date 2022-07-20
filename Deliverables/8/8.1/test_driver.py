# https://docs.python.org/3/howto/sockets.html
import sys, json, socket, threading
from typing import List

sys.path.append('../../../')
from my_python.Network import Network

from my_python.GenValidMove import GenValidMove
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState


#########################
#### Main game loop #####
#########################

### Read in network config from stdin
input_str = sys.stdin.read()
network_config = json.loads(input_str)
### Set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostbyname(socket.gethostname()), network_config["port"])
s.bind(address)
s.listen(network_config["players"])
### Print confirmation to stdout that server has been set up
sys.stdout.flush()
print(json.dumps("started"))
sys.stdout.flush()
### Connect to the clients
while True:
    # raise AssertionError(f"Got connection to {c}, {addr} successfully!")
    c, addr = s.accept()
    raise ValueError("got hereeeee")
    print(f"Got connection to {c}, {addr} successfully!")
all_players: List[PlayerAdapter] = []
### Set up the main game playing loop
def play_game(pa: PlayerAdapter):
    pa.play()

while True:
    for p in all_players:
        thread = threading.Thread(target=play_game, args=p)
        thread.start()











# print(input_str, file=sys.stderr)
# sys.stderr.write(input_str)
# sys.stderr.write(json.loads(input_str))
# network_config = json.loads(input_str)      # e.g., { "players" : ["simple-player"], "port" : 8103 }

# for player in players, MyServer.start():
# if not validate_move, then player cheated. return false for their score
# for validate move, we need to check the player state the player is currently at (ps1) against the one they are
#   sending to the server (ps2)

#players: list = network_config["players"]
#port: int = network_config["port"]
#s = Network.MyServer(players, port)
#s.start()
#
