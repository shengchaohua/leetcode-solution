# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:06:29 2018

@problem: lintcode No.2 尾部的零

@author: sheng
"""

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        zeroNum = 0
        for i in range(1, n):
            if n // 5 ** i > 0:
                zeroNum += n // (5 ** i)
            else:
                break
        return zeroNum