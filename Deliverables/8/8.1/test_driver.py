# https://docs.python.org/3/howto/sockets.html
import sys, json, socket, threading
from typing import List

sys.path.append('../../../')
from my_python.Network import Network

from my_python.GenValidMove import GenValidMove
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState



#
# def handle_client(client_socket, addr):
#     while True:
#         msg = client_socket.recv(8192)
#         if msg == "ack": break
#         print(addr, ' >> ', msg)
#         client_socket.send(json.loads(msg))
#     client_socket.close()
#
# host = socket.gethostname()
# port = network_config["port"]
# players = network_config["players"]
#
# s.bind((host, port))
# s.listen()
# print(json.dumps("started"))
#
# while True:
#     c, addr = s.accept()
#     print(f"Got connection to {c}, {addr} successfully!")
#     thread = threading.Thread(target=handle_client, args=(c, addr))
#     thread.start()
#     print(f"There are currently {threading.active_count()-1} active threads")



#########################
#### Main game loop #####
#########################
# all_players: List[PlayerAdapter] = []                   # list of PlayerAdapters
# each_player_still_playing_status: List[bool] = []       # list of booleans specifying whether we're still playing with each player
# while True in each_player_still_playing_status:
#     for i in range(len(all_players)):
#         pa = all_players[i]
#         pa.play()
#         if pa.game_over:
#             each_player_still_playing_status[i] = False


### Read in network config from stdin
input_str = sys.stdin.read()
network_config = json.loads(input_str)
### Set up the socket
s = socket.socket()
s.bind((socket.gethostname(), network_config["port"]))
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
