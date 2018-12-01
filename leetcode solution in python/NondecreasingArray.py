# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:17:30 2018

@problem: leetcode 665. Non-decreasing Array

@author: shengchaohua
"""

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(nums)-1 and nums[i] <= nums[i+1]:
            i += 1
        
        if i == len(nums)-1:
            return True
#        if i > 0 and i < len(nums) and 
        else:
            nums[i] = nums[i+1]
            while i < len(nums)-1 and nums[i] <= nums[i+1]:
                i += 1 
        
            return i == len(nums)-1
    

def test():
    s = Solution()
    nums = [3,4,2,3]
    print(s.checkPossibility(nums))


if __name__ == '__main__':
    test()