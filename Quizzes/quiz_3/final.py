from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        #同join加空格
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid)))) 
def display_good_grid():
    for i in range(len(good_grid)):
        print('   ', ' '.join(str(int(good_grid[i][j])) for j in range(len(good_grid))))
def triangles_in_grid():
    #声明是全局变量
    global good_grid
    global s
    global dim
    global max_size
    bei = 0
    nan = 0
    dong = 0
    xi = 0
    size_woqc = []
    am_N = 0
    A = []
    for i in range(max_size-1,len(good_grid)-max_size+1):
        for j in range(max_size-1,len(good_grid)-max_size+1):
            for k in range(max_size,1,-1):
                A.append(0)
                for m in range(0,k):
                    for n in range(-m,m+1):
                        bei = bei + good_grid[i+m][j+n]
                if bei == k*k:
                    by_grid_bei[k-1][1] = by_grid_bei[k-1][1] + 1
                    by_grid_bei[k-1][0] = k
                    bei = 0
                    break
                else:
                    bei = 0
    for i in range(max_size-1,len(good_grid)-max_size+1):
        for j in range(max_size-1,len(good_grid)-max_size+1):
            for k in range(max_size,1,-1):
                A.append(0)
                for m in range(0,k):
                    for n in range(-m,m+1):
                        nan = nan + good_grid[i-m][j+n]
                if nan == k*k:
                    by_grid_nan[k-1][1] = by_grid_nan[k-1][1] + 1
                    by_grid_nan[k-1][0] = k
                    nan = 0
                    break
                else:
                    nan = 0
    for i in range(max_size-1,len(good_grid)-max_size+1):
        for j in range(max_size-1,len(good_grid)-max_size+1):
            for k in range(max_size,1,-1):
                A.append(0)
                for m in range(0,k):
                    for n in range(-m,m+1):
                        dong = dong + good_grid[i+n][j-m]
                if dong == k*k:
                    by_grid_dong[k-1][1] = by_grid_dong[k-1][1] + 1
                    by_grid_dong[k-1][0] = k
                    dong = 0
                    break
                else:
                    dong = 0
    for i in range(max_size-1,len(good_grid)-max_size+1):
        for j in range(max_size-1,len(good_grid)-max_size+1):
            for k in range(max_size,1,-1):
                A.append(0)
                for m in range(0,k):
                    for n in range(-m,m+1):
                        xi = xi + good_grid[i+n][j+m]
                if xi == k*k:
                    by_grid_xi[k-1][1] = by_grid_xi[k-1][1] + 1
                    by_grid_xi[k-1][0] = k
                    xi = 0
                    break
                else:
                    xi = 0
    prtraingel = defaultdict(list)
    #以列表的形式 2点好处 1.append的时候对应键
    #可以不存在 2.append的时候不替换值 而是添加值
    for i in range(len(by_grid_bei)-1,-1,-1):
        if by_grid_bei[i][0] != 0:
            prtraingel['N'].append(by_grid_bei[i])
    for i in range(len(by_grid_nan)-1,-1,-1):
        if by_grid_nan[i][0] != 0:
            prtraingel['S'].append(by_grid_nan[i])
    for i in range(len(by_grid_dong)-1,-1,-1):
        if by_grid_dong[i][0] != 0:
            prtraingel['E'].append(by_grid_dong[i])
    for i in range(len(by_grid_xi)-1,-1,-1):
        if by_grid_xi[i][0] != 0:
            prtraingel['W'].append(by_grid_xi[i])
    return prtraingel

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
if dim%2 == 0:
    dc = dim - 1
else:
    dc = dim
max_size = int((dc + 1)/2)
by_grid_bei = [[0,0] for _ in range(max_size)]
by_grid_nan = [[0,0] for _ in range(max_size)]
by_grid_xi = [[0,0] for _ in range(max_size)]
by_grid_dong = [[0,0] for _ in range(max_size)] 
good_grid = [[0]*(dim+(max_size-1)*2) for _ in range(dim+(max_size-1)*2)]
for i in range(dim):
    for j in range(dim):
        good_grid[i+max_size-1][j+max_size-1] = 1 if grid[i][j] != 0 else 0
print('Here is the grid that has been generated:')
display_grid()
display_good_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have: ')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')