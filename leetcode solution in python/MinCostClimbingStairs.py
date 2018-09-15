# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 08:18:44 2018

@problem: leetcode 746. Min Cost Climbing Stairs

@author: shengchaohua
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
        