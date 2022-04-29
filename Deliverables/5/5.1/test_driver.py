import sys
sys.path.append('../../../')
from my_python.a5.GenValidMove import *

inp_lst = json.loads(sys.stdin.read())
# inp_lst = json.loads(open('../../../my_python/a5/test.json', 'r').read())
inp_gs = inp_lst[0]
inp_ps = inp_lst[1]
gs = GameState(inp_gs)
ps = PlayerState(inp_ps)

# returns a player state: either with the valid move,
#   or incrementing refusals.
print(GenValidMove(gs, ps))
# PlayerState(json.loads(str(GenValidMove(gs,ps))))

# open('../../../my_python/a5/test_output.json', 'w').\
#     write(str(GenValidMove(gs, ps)))

