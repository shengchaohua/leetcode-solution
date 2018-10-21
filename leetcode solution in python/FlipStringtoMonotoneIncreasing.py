# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:46:57 2018

@problem: leetcode 926. Flip String to Monotone Increasing

@author: shengchaohua
"""

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n_zero = n_one = 0
        for s in S:
            if s == "0":
                n_one = min(n_one, n_zero) + 1;
            else:
                n_one = min(n_one, n_zero)
                n_zero += 1
                
        return min(n_one, n_zero)
    
    
def test():
    s = Solution()
    S = "0001100010"
    print(s.minFlipsMonoIncr(S))
    
    
if __name__ == '__main__':
    test()