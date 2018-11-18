# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:27:10 2018

@problem: leetcode 941. Valid Mountain Array

@author: shengchaohua
"""

class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 1
        while i < len(A) and A[i-1] < A[i]:
            i += 1
        if i == 1 or i == len(A):
            return False
        while i < len(A) and A[i-1] > A[i]:
            i += 1
        return i == len(A)