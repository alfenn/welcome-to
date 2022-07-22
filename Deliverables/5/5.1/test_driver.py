import sys, json
sys.path.append('../../../')
from my_python.GameState import GameState
from my_python.PlayerState import PlayerState
from my_python.MoveGeneratorInterface import MoveGenerator1

inp_lst = json.loads(sys.stdin.read())
# inp_lst = json.loads(open('input_00_robby.json', 'r').read())
inp_gs = inp_lst[0]
inp_ps = inp_lst[1]
gs = GameState(inp_gs)
ps = PlayerState(inp_ps=inp_ps)

# returns a player state: either with the valid move,
#   or incrementing refusals.
print(MoveGenerator1().generate(gs, ps))

