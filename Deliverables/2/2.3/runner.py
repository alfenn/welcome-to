import sys, json
from pprint import pprint

from sort import sort

"""
Reads JSON objects from JSON string and stores them into
an array as dictionaries.

Arguments:
    JSON string

Returns:
    Array of dicts
"""


def parse_objects(json_str):
    # Convert JSON string into an array of JSON objects, filtering out all objects
    tokens = []
    reading_dict = False
    t = ''
    in_str = False
    for char in json_str:
        if char == '{':
            reading_dict = True
        if reading_dict:
            t += char
        if char == '"':
            if in_str is False:
                in_str = True
            else:
                in_str = False
        if char == '}':
            if reading_dict and in_str is False:
                tokens.append(t)
                t = ''
                reading_dict = False

    # Convert array of JSON objects into an array of dicts
    for i in range(len(tokens)):
        # json.load() takes a filepath
        # json.loads() takes a string
        try:
            tokens[i] = json.loads(tokens[i])
        except:
            sys.stderr.write(tokens[i])
    return tokens


"""
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
"""


def front_end():
    tokens = parse_objects(sys.stdin.read())
    # tokens = parse_objects(open('input1.json', 'r').read())

    # Discard non-special JSON objects
    to_remove = []
    for t in tokens:
        #   python uses short-circuit evaluation when evaluating and/or statements
        if ((t.keys() != {"content": 1}.keys())  # checks number of key-value pairs, and the keys
                or not (1 <= t.get("content") <= 24)):
            to_remove.append(t)
    tokens = [e for e in tokens if e not in to_remove]

    # Discard extra elements
    num_extra = len(tokens) % 10
    if num_extra != 0:
        tokens = tokens[: -num_extra]

    # Group tokens into groups of 10
    grouped_tokens = []
    for i in range(len(tokens) // 10):
        temp = []
        for j in range(10):
            temp.append(tokens[10 * i + j])
        grouped_tokens.append(temp)

    # Sort each group of tokens in place using the backend
    for i in range(len(grouped_tokens)):
        sort(grouped_tokens[i])

    # Return grouped tokens as json
    grouped_tokens = json.dumps(grouped_tokens)
    print(grouped_tokens)
    # Testing...
    # expect_out = json.dumps(json.loads(open('output1.json', 'r').read()))
    # print(expect_out == grouped_tokens)


front_end()
