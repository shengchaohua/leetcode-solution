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
        # Wrong Answer
        i = 0
        while i < len(nums)-1 and nums[i] <= nums[i+1]:
            i += 1
        if i == len(nums)-1:
            return 0
        first = i
        last = i + 1
        i += 1
        
        while i < len(nums)-1:
            
            while i < len(nums)-1 and nums[i] < nums[i+1]:         
                i += 1
            if i != len(nums)-1:
                last = i + 1
            i += 1
            
        return last - first + 1
    
    
def test():
    s = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15, 12]
    print(s.findUnsortedSubarray(nums))
    
    nums = [1, 3, 2, 2, 2, 4, 4]
    print(s.findUnsortedSubarray(nums))
    
    
if __name__ == '__main__':
    test()