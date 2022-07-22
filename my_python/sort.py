
"""
Consumes a list of 10 special JSON objects and sorts them in
ascending order based on the numerical value of their content
member.

Args:
    A list of 10 special JSON objects

Returns:
    None
"""


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