# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:11:08 2018

@problem: leetcode No.617 Merge Two Binary Trees

@author: shengchaohua
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 结点都为空时
        if t1 is None and t2 is None:
            return
        # 只有一个结点为空时
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        # 结点重叠时
        t1.val += t2.val
        # 进行迭代
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    
def main():
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t1_1 = TreeNode(11)
    t1_2 = TreeNode(12)
    t2_1 = TreeNode(21)
    t1.left = t1_1
    t1.right = t1_2
    t2.left = t2_1
    res = s.mergeTrees(t1, t2)
    print(res.val, res.left.val, res.right.val)
    
if __name__ == '__main__':
    main()