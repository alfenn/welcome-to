import sys, json, socket

sys.path.append('../../../')
from my_python.Network import Network
from my_python.GenValidMove import GenValidMove
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState
from my_python.player_adapters import RemotePlayerAdapter


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

