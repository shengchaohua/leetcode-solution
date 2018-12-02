# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:29:10 2018

@problem: leetcode 951. Flip Equivalent Binary Trees

@author: shengchaohua
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.check(root1, root2)
             
    def check(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None and node2 != None:
            return False
        elif node1 != None and node2 == None:
            return False
        if node1.val != node2.val:
            return False
    
        if self.check(node1.left, node2.left):
            return self.check(node1.right, node2.right)
        elif self.check(node1.left, node2.right):
            return self.check(node1.right, node2.left)
        else:
            return False
        