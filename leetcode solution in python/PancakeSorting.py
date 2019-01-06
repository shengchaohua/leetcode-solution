# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:40:19 2019

@problem: leetcode 969. Pancake Sorting

@author: shengchaohua
"""

class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flips = []
        for i in range(len(A)):
            max_ind = A.index(max(A[0:len(A)-i]))
            self.flip(A, max_ind+1)
            self.flip(A, len(A)-i)
            flips.extend([max_ind+1, len(A)-i])
        return flips
            
    
    def flip(self, A, k):
        left, right = 0, k-1
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    

def test():
    s = Solution()
    A = [3,2,4,1]
    print(s.pancakeSort(A))
    
    
if __name__ == '__main__':
    test()
    