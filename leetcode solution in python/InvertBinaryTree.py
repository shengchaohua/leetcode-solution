# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 14:47:18 2019

@problem: leetcode 226. Invert Binary Tree

@author: shengchaohua
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Recursive solution
#        if not root:
#            return None
#        root.left, root.right = root.right, root.left
#        self.invertTree(root.left)
#        self.invertTree(root.right)
#        return root
        
        # Iterative solution
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
    