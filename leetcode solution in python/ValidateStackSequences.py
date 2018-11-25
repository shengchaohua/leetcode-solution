# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:15:33 2018

@problem: leetcode 946. Validate Stack Sequences

@author: shengchaohua
"""

class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()
                
        return stack == []
    
    
def test():
    s = Solution()
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(s.validateStackSequences(pushed, popped))
    
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print(s.validateStackSequences(pushed, popped))
    

if __name__ == '__main__':
    test()
