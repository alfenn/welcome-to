import sys, json
sys.path.append('../../../')
from my_python.OldGameState import OldGameState
from my_python.PlayerState import PlayerState
from my_python.GenValidMove import GenValidMove

inp_lst = json.loads(sys.stdin.read())
# inp_lst = json.loads(open('input_00_robby.json', 'r').read())
inp_gs = inp_lst[0]
inp_ps = inp_lst[1]
gs = OldGameState(inp_gs)
ps = PlayerState(inp_ps=inp_ps)

# returns a player state: either with the valid move,
#   or incrementing refusals.
print(GenValidMove(gs, ps))

# open('test_output.json', 'w').\
#    write(str(GenValidMove(gs, ps)))

# PlayerState(json.loads(str(GenValidMove(gs,ps))))

