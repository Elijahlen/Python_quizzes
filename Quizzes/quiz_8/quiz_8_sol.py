# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner():
    directions = {'N': (-1, 0),'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    next_directions = {'': ('S', 'E'), 'N': ('E', 'N', 'W'), 'S': ('W', 'S', 'E'), 'E': ('S', 'E', 'N'), 'W': ('N', 'W', 'S')}
    if not grid[0][0]:
        return []
    paths = Queue()
    paths.enqueue(([(0, 0)], ''))
    while not paths.is_empty():
        path, previous_direction = paths.dequeue()
        x, y = path[-1]
        for new_direction in next_directions[previous_direction]:
            next_x, next_y = x + directions[new_direction][0], y + directions[new_direction][1]
            if next_x not in range(10) or next_y not in range(10):
                continue
            if (next_x, next_y) in path:
                continue
            if not grid[next_x][next_y]:
                continue
            path_copy = list(path)
            path_copy.append((next_x, next_y))
            paths.enqueue((path_copy, new_direction))
    return path

provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')
           
