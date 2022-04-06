import sys, json
from pprint import pprint

'''
Consumes a list of 10 special JSON objects and sorts them in 
ascending order based on the numerical value of their content 
member.

Args:
    A list of 10 special JSON objects

Returns:
    None
'''


def sort(data):
    # implement bubble sort
    num_iter = 0

    swapped = True
    # stop looping if there's a run with no swaps (swapped == F)
    while swapped:
        swapped = False
        for j in range(len(data) - num_iter - 1):
            if data[j].get('content') > data[j + 1].get('content'):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        num_iter += 1


'''
Your test driver should read 10 special JSON objects from 
STDIN, pass them to the back-end service, and display 
the result in STDOUT as a JSON array of 10 objects.

Arguments:
    A series of 10 special JSON objects

Returns:
    None
'''


def driver():
    # input = sys.stdin.read()
    input_str = open('input1.json', 'r').read()
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


driver()