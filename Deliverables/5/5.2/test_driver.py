import sys, json

sys.path.append("../../../")
from my_python.PlayerState import PlayerState
from my_python.calc_score import calc_score

inp_lst = json.loads(sys.stdin.read())
# inp_lst = json.loads(open('input_03_01_bis_robby.json', 'r').read())
inp_ps = inp_lst[0]
inp_temps = inp_lst[1]
ps = PlayerState(inp_ps=inp_ps)

print(calc_score(ps, inp_temps))

# open('../../../my_python/a5/test_output.json', 'w').\
#    write(str(GenValidMove(gs, ps)))

# PlayerState(json.loads(str(GenValidMove(gs,ps))))
