import sys
sys.path.append('../../../')
from my_python.PlayerState import PlayerState
from my_python.exceptions import InvalidMove
from my_python.GameState import GameState
from my_python.validate_move import validate_move
import json

input_str = sys.stdin.read()
# input_str = open('input_valid2.json', 'r').read()
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

### No try-except to let us see the error message
# validate_move(ps1, ps2, gs)
# print("true")
