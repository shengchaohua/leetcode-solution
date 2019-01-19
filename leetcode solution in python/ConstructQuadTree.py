# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:29:36 2019

@problem: leetcode 427. Construct Quad Tree

@author: shengchaohua
"""


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if self.isLeaf(grid):
        	return Node(grid[0][0] == 1, True, None, None, None, None)
        N = len(grid)
        return Node('*',
                    False,
                    self.construct([row[:N//2] for row in grid[:N//2]]),
                    self.construct([row[N//2:] for row in grid[:N//2]]),
                    self.construct([row[:N//2] for row in grid[N//2:]]),
                    self.construct([row[N//2:] for row in grid[N//2:]]))
        
    def isLeaf(self, grid):
        vals = set()
        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		vals.add(grid[i][j])
        		if len(vals) > 1: return False
       	return True

#        if all(grid):
#            return Node(True, True, None, None, None, None)
#        elif not any(grid):
#            return Node(False, True, None, None, None, None)
#        N = len(grid)
#        N = len(grid)
#        return Node('*', 
#                    False, 
#                    self.construct([[grid[i][j] for j in range(N//2)] for i in range(N//2)]),
#                    self.construct([[grid[i][j] for j in range(N//2, N)] for i in range(N//2)]),
#                    self.construct([[grid[i][j] for j in range(N//2)] for i in range(N//2, N)]),
#                    self.construct([[grid[i][j] for j in range(N//2, N)] for i in range(N//2, N)]))

def test():
    s = Solution()
    grid = [[1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0]]
    root = s.construct(grid)
#    root = Node('non_leaf', False, None, None, None, None)
#    root.topLeft = Node('non_leaf', True, None, None, None, None)
#    root.topRight = Node('non_leaf', True, None, None, None, None)
#    root.bottomLeft = Node('non_leaf', True, None, None, None, None)
#    root.bottomRight = Node('non_leaf', True, None, None, None, None)
    print('main')
    queue = [root]
    while queue:
        node = queue.pop(0)
        print("val: %s isLeaf: %s" % (node.val, node.isLeaf))
        if not node.isLeaf:
            queue.append(node.topLeft)
            queue.append(node.topRight)
            queue.append(node.bottomLeft)
            queue.append(node.bottomRight)
    

if __name__ == '__main__':
    test()