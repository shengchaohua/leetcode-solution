# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:56:09 2019

@problem: leetcode 783. Minimum Distance Between BST Nodes

@author: shengchaohua
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = root
        node_stack = []
        values = []
        while node or node_stack:
            if node:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                values.append(node.val)
                node = node.right
        
        return abs(min([values[i]-values[i+1] for i in range(len(values)-1)],
                        key=abs))
        
        # Solution from @aosingh
#        diff = float('inf') # Largest possible difference
#        last_visited_node = None # Track the last visited node in the sorted sequence to calculate difference in between adjacent elements. 
#        stack = [] # For Iterative in-order traversal
#        node = root
#        while stack or node is not None:
#            if node is not None:
#                stack.append(node)
#                node = node.left
#            else:
#                node = stack.pop()
#                if last_visited_node and node.val - last_visited_node.val < diff:
#                    diff = node.val - last_visited_node.val  
#                last_visited_node = node
#                node = node.right
#        return diff
                    