import json
import sys
sys.path.append('../../../')

from my_python.a3.GameState import *

input_str = sys.stdin.read()
# input_str = open('input1.json', 'r').read()

# json.load() takes a filepath
# json.loads() takes a string
j = json.loads(input_str)
try:
    GameState(j)
    print(input_str)
except:
    print("false")
