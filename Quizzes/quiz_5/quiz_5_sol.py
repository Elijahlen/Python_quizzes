# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by Eric Martin for COMP9021

import sys
from random import seed, randint


dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))


def explore_from(i, j):
    grid[i][j] += 2
    area = 1
    if i and grid[i - 1][j] == grid[i][j] - 2:
        area += explore_from(i - 1, j)
    if i < dim - 1 and grid[i + 1][j] == grid[i][j] - 2:
        area += explore_from(i + 1, j)
    if j and grid[i][j - 1] == grid[i][j] - 2:
        area += explore_from(i, j - 1)
    if j < dim - 1 and grid[i][j + 1] == grid[i][j] - 2:
        area += explore_from(i, j + 1)
    return area
    
def explore_again_from(i, j):
    color = grid[i][j]
    grid[i][j] += 2
    area = 1
    if i and grid[i - 1][j] == 1 - color:
        area += explore_again_from(i - 1, j)
    if i < dim - 1 and grid[i + 1][j] == 1 - color:
        area += explore_again_from(i + 1, j)
    if j and grid[i][j - 1] == 1 - color:
        area += explore_again_from(i, j - 1)
    if j < dim - 1 and grid[i][j + 1] == 1 - color:
        area += explore_again_from(i, j + 1)
    return area


try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner  = 0
size_of_largest_homogenous_region_from_top_left_corner = explore_from(0, 0)
print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = 0
for i in range(dim):
    for j in range(dim):
        grid[i][j] = grid[i][j] % 2
for i in range(dim):
    for j in range(dim):
        if grid[i][j] < 2:
            max_size_of_region_with_checkers_structure =\
                max(max_size_of_region_with_checkers_structure, explore_again_from(i, j))
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )




            

