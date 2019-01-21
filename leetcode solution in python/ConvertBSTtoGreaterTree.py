# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:58:23 2019

@problem: leetcode 538. Convert BST to Greater Tree

@author: shengchaohua
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursive solution
#    def __init__(self):
#        self.total = 0
#
#    def convertBST(self, root):
#        if root is not None:
#            self.convertBST(root.right)
#            self.total += root.val
#            root.val = self.total
#            self.convertBST(root.left)
#        return root

    # My solution
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Iteration with a Stack
#        total = 0
#        node = root
#        stack = []
#        while stack or node:
#            # push all nodes up to (and including) this subtree's maximum on
#            # the stack.
#            while node:
#                stack.append(node)
#                node = node.right
#    
#            node = stack.pop()
#            total += node.val
#            node.val = total
#            # all nodes with values between the current and its parent lie in
#            # the left subtree.
#            node = node.left
#    
#        return root
        
        # My solution. Two in-roder traversal
        node = root
        node_stack = []
        changed_keys = []
        while node or node_stack:
            if node:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                changed_keys = [k + node.val for k in changed_keys]
                changed_keys.append(node.val)
                node = node.right
        
        node = root
        node_stack = []
        changed_keys = changed_keys[::-1]
        while node or node_stack:
            if node:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                node.val = changed_keys.pop()
                node = node.right
        
        return root
                
    
def test():
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    root = s.convertBST(root)
    node = root
    node_stack = []
    while node or node_stack:
        if node:
            node_stack.append(node)
            node = node.left
        else:
            node = node_stack.pop()
            print(node.val)
            node = node.right
    

if __name__ == '__main__':
    test()
    