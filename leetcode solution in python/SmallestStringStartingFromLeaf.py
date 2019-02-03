# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:33:46 2019

@problem: leetcode 988. Smallest String Starting From Leaf

@author: shengchaohua
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        def find(node):
            if not node:
                return ''
            elif not node.left and not node.right:
                return chr(node.val + 97)
            elif not node.left:
                return find(node.right) + chr(node.val + 97)
            elif not node.right:
                return find(node.left) + chr(node.val + 97)
            left = find(node.left)
            right = find(node.right)
            return min(left + chr(node.val + 97), right + chr(node.val + 97))
        
        return find(root)