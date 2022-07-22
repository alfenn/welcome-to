import sys, json
from pprint import pprint
sys.path.append('../../../')
from my_python.sort import sort

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
    num_nested_braces = 0
    num_nested_brackets = 0
    in_str = False
    in_arr = False
    for i in range(len(json_str)):
        char = json_str[i]
        # need to account for input3_team2 case where you have dictionaries as elements in an array
        # ... need to rethink logic here. you could either be in a nested array or a nested dict. we account for nested dicts already.
        # Set conditions for in_str.
        if char == '"':
            # Fixed out of bounds in java, but python list indexing accepts negative indices.
            #   Fine to leave like this because the last character of a valid .json can never be "\\".
            if json_str[i-1] != "\\":
                if not in_str: in_str = True
                else: in_str = False

        # Split the nested braces operations from reading_dict case below so we don't count first '{' as nested
        if reading_dict and not in_str:
            if char == '{':
                num_nested_braces += 1

        # If NOT currently reading a top-level dictionary.
        if not reading_dict and not in_str:
            if char == '[':
                if in_arr: num_nested_brackets += 1
                else: in_arr = True
            if char == '{' and not in_arr:
                reading_dict = True
            if char == ']':
                if num_nested_brackets != 0: num_nested_brackets -= 1
                else: in_arr = False

        # If currently reading a top-level dictionary.
        if reading_dict:
            t += char
            # Split this from the num_braces++ case above so we include the '}' in t.
            if not in_str and char == '}':
                if num_nested_braces == 0:
                    tokens.append(t)
                    t = ''
                    reading_dict = False
                # Check != 0 so we don't count actual closing '}' as nested.
                # Put this under the previous condition so { { {} } } doesn't chop off the last '}'
                if num_nested_braces != 0:
                    num_nested_braces -= 1

    # Convert array of JSON objects into an array of dicts
    for i in range(len(tokens)):
        # json.load() takes a filepath
        # json.loads() takes a string
        tokens[i] = json.loads(tokens[i])
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
    # TODO
    tokens = parse_objects(sys.stdin.read())
    # tokens = parse_objects(open('test.txt', 'r').read())

    # Discard non-special JSON objects
    to_remove = []
    for t in tokens:
        #   python uses short-circuit evaluation when evaluating and/or statements
        if ((t.keys() != {"content": 1}.keys())  # checks number of key-value pairs, and the keys
                or type(t.get("content")) != int
                or not (1 <= t.get("content") <= 24)):
            to_remove.append(t)
    # this has an issue, and tokens += e also has issue. need to use .append(e)
    # tokens = [e for e in tokens if e not in to_remove]
    tokens_copy = tokens
    tokens = []
    for e in tokens_copy:
        # this has an issue. it's saying the last input {1} is in to_remove when it's not
        # if e not in to_remove:
        in_to_remove = False
        for r in to_remove:
            # using == confuses 0 and 1 with F,T respectively. p sure that's the issue with 'in'
            if e is r:
                in_to_remove = True
                break
        if not in_to_remove:
            tokens.append(e)

    # TODO
    # pprint(tokens)

    # Discard extra elements
    num_extra = len(tokens) % 10
    if num_extra != 0:
        tokens = tokens[: -num_extra]
    # TODO
    # print(tokens)

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
