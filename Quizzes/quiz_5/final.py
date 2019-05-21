# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint


dim = 10
grid = [[None] * dim for _ in range(dim)]
def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

# Possibly define other functions

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
spare_grid = [[None] * dim for _ in range(dim)]
def real_copy(x,y):
    for i in range(dim):
        for j in range(dim):
            x[i][j] = y[i][j]
real_copy(spare_grid,grid)
def replace_1_by_gold(i,j):
    global dim
    if grid[i][j] == 1:
        grid[i][j] = '$'
        if i>0:
            replace_1_by_gold(i-1,j)
        if i<dim-1:
            replace_1_by_gold(i+1,j)
        if j>0:
            replace_1_by_gold(i,j-1)
        if j<dim-1:
            replace_1_by_gold(i,j+1)
def replace_0_by_gold(i,j):
    global dim
    if grid[i][j] == 0:
        grid[i][j] = '$'
        if i>0:
            replace_0_by_gold(i-1,j)
        if i<dim-1:
            replace_0_by_gold(i+1,j)
        if j>0:
            replace_0_by_gold(i,j-1)
        if j<dim-1:
            replace_0_by_gold(i,j+1)
if grid[0][0] == 1:
    replace_1_by_gold(0,0)
else:
    replace_0_by_gold(0,0)
    
def display_normal_grid():
    for i in range(dim):
        print('   ', ' '.join(str(grid[i][j]) for j in range(dim)))
display_normal_grid()
Acc = 0
for i in range(dim):
    for j in range(dim):
        if grid[i][j] == '$':
            Acc = Acc + 1
size_of_largest_homogenous_region_from_top_left_corner  = Acc
print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

real_copy(grid,spare_grid)
Bcc = 1
def count_chekers(i,j):
    global Bcc
    if grid[i][j] == 1:
        grid[i][j] = '*'
        if i>0:
            if grid[i-1][j] == 0:
                Bcc = Bcc+1
                count_chekers(i-1,j)
        if i<dim-1:
             if grid[i+1][j] == 0:
                Bcc = Bcc+1
                count_chekers(i+1,j)
        if j>0:
             if grid[i][j-1] == 0:
                Bcc = Bcc+1 
                count_chekers(i,j-1)
        if j<dim-1:
            if grid[i][j+1] == 0:
                Bcc = Bcc+1
                count_chekers(i,j+1)
    elif grid[i][j] == 0:
        grid[i][j] = '*'
        if i>0:
            if grid[i-1][j] == 1:
                Bcc = Bcc+1
                count_chekers(i-1,j)
        if i<dim-1:
             if grid[i+1][j] == 1:
                Bcc = Bcc+1
                count_chekers(i+1,j)
        if j>0:
             if grid[i][j-1] == 1:
                Bcc = Bcc+1
                count_chekers(i,j-1)
        if j<dim-1:
            if grid[i][j+1] == 1:
                Bcc = Bcc+1
                count_chekers(i,j+1)
    return Bcc
Ccc = 0
for i in range(dim):
    for j in range(dim):
        count_chekers(i,j)
        if count_chekers(i,j)>Ccc:
            Ccc = count_chekers(i,j)
        Bcc = 1
max_size_of_region_with_checkers_structure = Ccc
# Replace this comment with your code
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )
display_normal_grid()




            

