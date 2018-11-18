# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:05:31 2018

@problem: leetcode 942. DI String Match

@author: shengchaohua
"""

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        A = list(range(N+1))
        
        res = []
        for s in S:
            if s == 'I':
                res.append(A.pop(0))
            else:
                res.append(A.pop(len(A)-1))
        
        return res + A
    
    
def test():
    s = Solution()
    S = 'IDID'
    print(s.diStringMatch(S))
    
    
if __name__ == '__main__':
    test()
    