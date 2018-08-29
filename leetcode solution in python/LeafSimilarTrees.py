# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:32:12 2018

@problem: leetcode No.872 Leaf-Similar Trees

@author: shengchaohua
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
    def set_left(self, node):
        self.left = node
        
    def set_right(self, node):
        self.right = node

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.preOrder(root1) == self.preOrder(root2)        
        
    def preOrder(self, root):
        leaves = []
        if root:
            if root.left is None and root.right is None:
                leaves.append(root.val)
            leaves += self.preOrder(root.left)
            leaves += self.preOrder(root.right)
        return leaves

    
if __name__ == '__main__':
    pass