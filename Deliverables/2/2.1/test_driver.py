import sys, json
sys.path.append('../../../')
from my_python.sort import sort

"""
Your test driver should read 10 special JSON objects from 
STDIN, pass them to the back-end service, and display 
the result in STDOUT as a JSON array of 10 objects.

Arguments:
    A series of 10 special JSON objects

Returns:
    None
"""


input_str = sys.stdin.read()
# input_str = open('input1.json', 'r').read()
tokens = input_str.split('{')
tokens.pop(0)
for i in range(len(tokens)):
    tokens[i] = '{' + tokens[i]
for i in range(len(tokens)):
    # json.load() takes a filepath
    # json.loads() takes a string
    tokens[i] = json.loads(tokens[i])
sort(tokens)
tokens = json.dumps(tokens)
print(tokens)
