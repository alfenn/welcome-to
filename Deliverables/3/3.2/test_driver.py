import json
import sys
sys.path.append('../../../')
from my_python.OldGameState import OldGameState

# input_str = sys.stdin.read()
input_str = open('input_city-plans_b_1_robby.json', 'r').read()

# json.load() takes a filepath
# json.loads() takes a string
j = json.loads(input_str)
# try:
#     gs = OldGameState(j)
#     print(gs)
# except:
#     print("false")

gs = OldGameState(j)