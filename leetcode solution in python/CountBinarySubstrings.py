# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:17:33 2019

@problem: leetcode 696. Count Binary Substrings

@author: shengchaohua
"""

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Naive solution
#        count = 0
#        for i in range(len(s)-1):
#            if s[i:i+2] in ('01', '10'):
#                for j in range(min(i, len(s)-i-2)+1):
#                    if not (s[i-j] == s[i] and s[i+1] == s[i+1+j]):
#                        break
#                    count += 1
#                            
#        return count
        
        # Reference solution
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                groups[-1] += 1
            else:
                groups.append(1)

        count = 0
        for i in range(1, len(groups)):
            count += min(groups[i-1], groups[i])
        return count
        