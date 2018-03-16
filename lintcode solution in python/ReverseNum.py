# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:22:19 2018

@problem: lintcode No.37 reverse a 3-bit number

@author: sheng
"""

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        return int(str(number)[::-1])