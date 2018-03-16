# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:24:10 2018

@author: sheng
"""

class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        a, b = 0, 1
        for i in range(n-2):
            a, b = b, a + b
        return b if n > 1 else 0