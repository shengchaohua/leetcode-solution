# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 16:05:33 2019

@problem: leetcode 784. Letter Case Permutation

@author: shengchaohua
"""

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # The solution from @blehart
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res
    