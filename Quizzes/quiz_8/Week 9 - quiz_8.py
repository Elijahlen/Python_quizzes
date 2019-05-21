# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from stack_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner():
    pass
    global i
    global j
    global going_north
    global going_south
    global going_west
    global going_east
    global path
    if grid[0][0] == 0:
        return
    i = 0
    j = 0

    stack.push([(i,j)])
    real_path = []
    going_east = True
    L_pre = 0
    L_afterpush = 1
    while not stack.is_empty():
        if L_pre == L_afterpush:# get the end of branch
            for k in range(len(stack._data[-1])):
                if path[k] == stack._data[-1][k]:
                    i = stack._data[-1][k][0]
                    j = stack._data[-1][k][1]
                else:
                    break
        path = stack.pop()
        L_pre = len(stack)
        if path[-1][0] == i and path[-1][1] > j:
            going_east = True
        elif path[-1][0] == i and path[-1][1] < j:
            going_west = True
        elif path[-1][0] > i and path[-1][1] == j:
            going_south = True
        elif path[-1][0] < i and path[-1][1] == j:
            going_north = True
        i = path[-1][0]
        j = path[-1][1]
        print(path)
        if len(path)> len(real_path):
            real_path = path
        if check_adjacent():
            for m in list(reversed(check_adjacent())):
                stack.push(path + [m])
        L_afterpush = len(stack)
        going_north = False
        going_south = False
        going_west = False
        going_east = False
    return real_path
    # Replace pass above with your code
def check_adjacent():
    global i
    global j
    global going_north
    global going_south
    global going_west
    global going_east
    global path
    adjacent_list = []
    if going_east:
        if i > 0 : #north
            if grid[i-1][j]!=0 and not(((i-1,j)) in path):
                adjacent_list += [(i-1,j)]
        if j < 9 : #east
            if grid[i][j+1]!=0 and not(((i,j+1)) in path):
                adjacent_list += [(i, j+1)]
        if i < 9:  #south
            if grid[i+1][j] != 0 and not(((i+1,j)) in path):
                adjacent_list += [(i+1, j)]
        return adjacent_list
    if going_north:
        if j > 0  : #west
            if grid[i][j-1]!=0 and not(((i,j-1)) in path):
                adjacent_list += [(i, j-1)]
        if i > 0 : #north
            if grid[i - 1][j] != 0 and not (((i - 1, j)) in path):
                adjacent_list += [(i-1,j)]
        if j < 9 : #east
            if grid[i][j + 1] != 0 and not (((i, j + 1)) in path):
                adjacent_list += [(i, j+1)]
        return adjacent_list
    if going_west:
        if i < 9:  #south
            if grid[i + 1][j] != 0 and not (((i + 1, j)) in path):
                adjacent_list += [(i+1, j)]
        if j > 0  : #west
            if grid[i][j - 1] != 0 and not (((i, j - 1)) in path):
                adjacent_list += [(i, j-1)]
        if i > 0 : #north
            if grid[i - 1][j] != 0 and not (((i - 1, j)) in path):
                adjacent_list += [(i-1,j)]
        return adjacent_list
    if going_south:
        if j < 9 : #east
            if grid[i][j + 1] != 0 and not (((i, j + 1)) in path):
                adjacent_list += [(i, j+1)]
        if i < 9:  #south
            if grid[i + 1][j] != 0 and not (((i + 1, j)) in path):
                adjacent_list += [(i+1, j)]
        if j > 0  : #west
            if grid[i][j - 1] != 0 and not (((i, j - 1)) in path):
                adjacent_list += [(i, j-1)]
        return adjacent_list
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
lu = leftmost_longest_path_from_top_left_corner()
if not lu:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {lu}')
           
