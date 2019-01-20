# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 12:47:12 2019

@problem: leetcode 978. Longest Turbulent Subarray

@author: shengchaohua
"""

class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:
            return 1
        
        i = 0
        max_size = 1
        while i < len(A)-1:
            while i < len(A) - 1 and A[i] == A[i+1]:
                i += 1
                continue
            if i < len(A) - 1:
                flag = '>' if A[i] > A[i+1] else '<'
                i += 1
                size = 2
            while i < len(A) - 1:
                if (flag == '>' and A[i] >= A[i+1] or
                    flag == '<' and A[i] <= A[i+1]):
                    break
                elif flag == '>' and A[i] < A[i+1]:
                    size += 1
                    flag = '<'
                else: # flag =='<' and A[i] > A[i+1]
                    size += 1
                    flag = '>'
                i += 1
            if size > max_size:
                max_size = size
        return max_size
    
    
def test():
    s = Solution()
    nums = [9,4,2,10,7,8,6,8,8,1,9]
    print(s.maxTurbulenceSize(nums))
    nums = [4,8,12,16]
    print(s.maxTurbulenceSize(nums))
    

if __name__ == '__main__':
    test()
                
        