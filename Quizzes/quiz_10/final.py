# Written by *** for COMP9021


from binary_tree_adt import *
from math import log
from  collections import defaultdict

class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        pass
        index = self.size() + 1
        l = []
        if index == 1:
            self.value = value
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
            return
        while index > 1:
            if index % 2 == 0:
                l = l + ['l']
                index = index // 2
            elif index % 2 == 1:
                l = l + ['r']
                index = index // 2
        node = self
        l.reverse()
        s = 2
        for e in l:
            if e == 'l':
                node = node.left_node

            if e == 'r':
                node = node.right_node

        node.value = value
        node.left_node = BinaryTree()
        node.right_node = BinaryTree()

        for i in range(len(l)):
            bubble = self
            for b in l[:-(i+1)]:
                if b == 'l':
                    bubble = bubble.left_node
                if b == 'r':
                    bubble = bubble.right_node
            if l[-(i+1)] == 'l' and bubble.value > bubble.left_node.value:
                inter = bubble.value
                bubble.value = bubble.left_node.value
                bubble.left_node.value = inter
            elif l[-(i+1)] == 'r' and bubble.value > bubble.right_node.value:
                inter = bubble.value
                bubble.value = bubble.right_node.value
                bubble.right_node.value = inter
        return
