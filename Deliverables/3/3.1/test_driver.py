import sys
sys.path.append('../../../')
from my_python.PlayerState import PlayerState
import json

input_str = sys.stdin.read()
# input_str = open('input1.json', 'r').read()

# json.load() takes a filepath
# json.loads() takes a string
j = json.loads(input_str)
try:
    PlayerState(inp_ps=j)
    print(input_str)
except:
    print("false")
