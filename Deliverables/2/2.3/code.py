import sys, json
from pprint import pprint

# append the path of the
# parent directory

from Deliverables.proj_lib.backend.sort import sort


'''
Reads JSON values from STDIN and, once STDIN is closed,
filters out all but the special-object JSON objects,
splits the JSON values that remains into groups of 10,
respecting the order in which they were provided through
STDIN, with leftover objects being discarded.

Then, uses back-end sort component to sort each remaining
group and outputs the sorted groups as a single JSON array
that contains JSON arrays with 10 objects each.

Arguments:
    None

Returns:
    None
'''


def front_end():
    input_str = sys.stdin.read()
    # input_str = open('input6.json', 'r').read()
    tokens = input_str.split('{')
    tokens.pop(0)

    # convert tokens to an array of dictionaries
    for i in range(len(tokens)):
        tokens[i] = '{' + tokens[i]
    for i in range(len(tokens)):
        # json.load() takes a filepath
        # json.loads() takes a string
        tokens[i] = json.loads(tokens[i])

    # discard non special-object-JSON elements
    to_remove = []
    for t in tokens:
        #   python uses short-circuit evaluation when evaluating and/or statements
        if (isinstance(t, dict)
                or (t.keys() != {"content": 1}.keys())  # checks number of key-value pairs, and the keys
                or not (1 <= t.get("content") <= 24)):
            to_remove.append(t)
    tokens = [e for e in tokens if e not in to_remove]

    # discard extra elements
    num_extra = len(tokens) % 10
    if num_extra != 0:
        tokens = tokens[: -num_extra]

    # group tokens into groups of 10
    grouped_tokens = []

    for i in range(len(tokens) // 10):
        temp = []
        for j in range(10):
            temp.append(tokens[10 * i + j])
        grouped_tokens.append(temp)

    # sort each group of tokens in place using the backend
    for i in range(len(grouped_tokens)):
        sort(grouped_tokens[i])

    grouped_tokens = json.dumps(grouped_tokens)
    print(grouped_tokens)
    # expect_out = json.dumps(json.loads(open('output6.json', 'r').read()))
    # print(expect_out == grouped_tokens)


front_end()
