# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 08:50:03 2018

@problem: leetcode 581. Shortest Unsorted Continuous Subarray

@author: shengchaohua
"""

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        start, end = len(nums)-1, 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end > start else 0
    
    
def test():
    s = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(s.findUnsortedSubarray(nums))
    
    nums = [1, 3, 2, 2, 2, 4, 4]
    print(s.findUnsortedSubarray(nums))
    
    
if __name__ == '__main__':
    test()