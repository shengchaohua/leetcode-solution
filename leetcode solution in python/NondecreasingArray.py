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
        # Brute solution. TLE!
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        new = nums[:]
        for i in range(len(nums)):
            old_ai = nums[i]
            new[i] = new[i-1] if i > 0 else float('-inf')
            if monotone_increasing(new):
                return True
            new[i] = old_ai

        return False
    
    def checkPossibility2(self, nums):
        # Locate and Analyze Problem Index
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]) 
    

def test():
    s = Solution()
    nums = [3,4,2,3]
    print(s.checkPossibility(nums))
    print(s.checkPossibility2(nums))


if __name__ == '__main__':
    test()