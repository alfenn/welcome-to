import sys
sys.path.append('../../../')
from my_python.a5.GenValidMove import *

inp_lst = json.loads(input())
inp_gs = inp_lst[0]
inp_ps = inp_lst[1]
gs = GameState(inp_gs)
ps = PlayerState(inp_ps)

# returns a player state: either with the valid move,
#   or incrementing refusals.
print(GenValidMove(gs, ps))

