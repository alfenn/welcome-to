import sys
sys.path.append('../../../')
from my_python.PlayerState import PlayerState
from my_python.exceptions import InvalidPlayerState
import json

input_str = sys.stdin.read()
# input_str = open('test.json', 'r').read()

# json.load() takes a filepath
# json.loads() takes a string
j = json.loads(input_str)
try:
    ps = PlayerState(inp_ps=j)
    print(ps)
except:
    print("false")
