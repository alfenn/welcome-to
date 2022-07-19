import sys, json, socket

sys.path.append('../../../')
from my_python.Network import Network

from my_python.GenValidMove import GenValidMove
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState

#class ServerAdaptor():
 #   def __init__(self, serv: MyServer, ):




# for player in players, MyServer.start():
# if not validate_move, then player cheated. return false for their score
# for validate move, we need to check the player state the player is currently at (ps1) against the one they are
#   sending to the server (ps2)

# network_config = json.loads(sys.stdin.read())
network_config = { "players" : ["simple-player"], "port" : 8103 }
players: list = network_config["players"]
port: int = network_config["port"]
s = Network.MyServer(players, port)
s.start()

