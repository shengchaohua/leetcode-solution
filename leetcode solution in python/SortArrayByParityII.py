# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:10:38 2018

@problem: leetcode 922. Sort Array By Parity II

@author: shengchaohua
"""

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        while i < len(A) and j < len(A):
            while i < len(A) and A[i] % 2 == 0:
                i += 2
            
            while j < len(A) and A[j] % 2 == 1:
                j +=2
            
            if i < len(A) and j <len(A):
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
            

def test():
    s = Solution()
    A = [4, 2, 5, 7]
    s.sortArrayByParityII(A)
    print(A)
    

if __name__ == '__main__':
    test()