import sys, json, socket

sys.path.append('../../../')
from my_python.Network import MyServer
from my_python.GenValidMove import GenValidMove
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState

#class RemoteServerAdaptor():
 #   def __init__(self):



# for player in players, MyServer.start():
# if not validate_move, then player cheated. return false for their score

network_config = json.loads(sys.stdin.read())
# input_str = open('input9_team9.json', 'r').read()
players: network_config["players"]
port: int = network_config["port"]
# Initialize remote player adapter with network connectivity and a game-playing
# function
s = MyServer(players,port)
s.start()

