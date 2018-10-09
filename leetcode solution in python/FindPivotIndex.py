# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:24:03 2018

@problem: leetcode 724. Find Pivot Index

@author: shengchaohua
"""

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = sum(nums)

        for i, n in enumerate(nums):
            if i > 0:
                left_sum += nums[i-1]
            right_sum -= n
            if left_sum == right_sum:
                return i
            
        return -1
    
    
def test():
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(s.pivotIndex(nums))
    nums = [1, 2, 3]
    print(s.pivotIndex(nums))
    nums = [1]
    print(s.pivotIndex(nums))
    nums = [1, 0]
    print(s.pivotIndex(nums))
    nums = [0, 1]
    print(s.pivotIndex(nums))
    
    
if __name__ == '__main__':
    test()