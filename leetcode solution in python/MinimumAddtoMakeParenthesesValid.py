# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:33:21 2018

@problem: leetcode 921. Minimum Add to Make Parentheses Valid

@author: shengchaohua
"""

class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = []
        num = 0
        for s in S:
            if s == '(':
                l.append(s)
            if s == ')' :
                if l and l[-1] == '(':
                    l.pop()
                else:
                    num += 1
        
        return num + len(l)
    
    
def test():
    s = Solution()
    S = "()))(("
    print(s.minAddToMakeValid(S))
                

if __name__ == '__main__':
    test()