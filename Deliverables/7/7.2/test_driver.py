import json
import sys
sys.path.append('../../../')
from my_python.GameState import GameState

input_str = sys.stdin.read()
# input_str = open('input_invalid2_score.json', 'r').read()
# input_str = open('../../3/3.2/input_incorrect_4_test_team1.json', 'r').read()

# json.load() takes a filepath
# json.loads() takes a string
j = json.loads(input_str)
try:
    gs = GameState(j)
    print(gs)
except:
    print("false")

# gs = GameState(j)
# print(gs)
