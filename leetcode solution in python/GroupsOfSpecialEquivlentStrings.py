# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:46:48 2018

@problem: leetcode 893. Groups of Special-Equivalent Strings

@author: shengchaohua
"""

class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len({tuple(sorted(s[0::2]) + sorted(s[1::2])) for s in A})
    
    def isSpecialEquivlent(s1, s2):
        if s1 == s2:
            return True
        
#        for i, letter in enumerate(s1):
#            ind = s2.find(letter)
#            if ind == -1 or ind % 2 != i % 2::
#                return false
#            else:
#                pass
#        
#        return True
                
        
                
    