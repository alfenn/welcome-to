import sys, json
sys.path.append('../../../')

from my_python.PlayerState import PlayerState

input_str = sys.stdin.read()
# input_str = open('../../3/3.1/input_bis_g_1_robby.json', 'r').read()
# input_str = open('input_roundabout_g_8_robby.json', 'r').read()
j = json.loads(input_str)
try:
    ps = PlayerState(inp_ps=j)
    print(ps)
except:
    print("false")
# For debugging- let error show
# PlayerState(inp_ps=j)
