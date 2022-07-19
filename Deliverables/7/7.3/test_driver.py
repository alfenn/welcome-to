import sys

sys.path.append('../../../')
from my_python.PlayerState import PlayerState
from my_python.exceptions import InvalidMove
from my_python.GameState import GameState
from my_python.validate_move import validate_move
import json

input_str = sys.stdin.read()
# input_str = open('input_07_04_adv-two-streets-all-pools_robby.json', 'r').read()
# input_str = open('input_b_1_team24.json', 'r').read()
inp_lst = json.loads(input_str)
inp_gs = inp_lst[0]
inp_ps1 = inp_lst[1]
inp_ps2 = inp_lst[2]
gs: GameState = GameState(inp_gs)
ps1: PlayerState = PlayerState(inp_ps=inp_ps1)
ps2: PlayerState = PlayerState(inp_ps=inp_ps2)

try:
    validate_move(ps1, ps2, gs)
    print("true")
except InvalidMove:
    print("false")

# validate_move(ps1, ps2, gs)
