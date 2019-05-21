# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *
# Possibly define some functions
def finding_leaves(tree):
    if tree.value is None:
        return []
    values = []
    if tree.left_node.value is None and tree.right_node.value is None:
        values = values + [tree.value]
    values.extend(finding_leaves(tree.left_node))
    values.extend(finding_leaves(tree.right_node))
    return values
def max_diff_in_consecutive_leaves(tree):
    pass
    list = finding_leaves(tree)
    if len(list)<=1:
        return 0
    diff = 0
    for i in range(1,len(list)):
        if abs(list[i]-list[i-1]) > diff:
            diff = abs(list[i]-list[i-1])
    return diff
    # Replace pass above with your code


provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
