import sys, json
sys.path.append('../../../')
from my_python.players_adaptors_translators import RemotePlayerAdapter
from my_python.MoveGeneratorInterface import MoveGenerator1


network_config = json.loads(sys.stdin.read())
HOST = network_config["host"]
PORT = network_config["port"]
rpa = RemotePlayerAdapter(MoveGenerator1(), HOST, PORT)
rpa.play()
