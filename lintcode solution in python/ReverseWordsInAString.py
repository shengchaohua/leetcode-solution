# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 08:32:07 2018

@problem: lintcode 53 53. Reverse Words in a String

@author: sheng
"""

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        sArr = s.strip().split(' ')
        sArr.reverse()
        arr = [sa for sa in sArr if sa != '']
        return ' '.join(arr)