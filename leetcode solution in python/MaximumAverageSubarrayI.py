# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:03:34 2018

@problem: leetcode 643. Maximum Average Subarray I

@author: shengchaohua
"""

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = sum(nums[0:k])
        temp = max_sum
        
        i = k
        while i < len(nums):
            temp = temp - nums[i-k] + nums[i]
            i += 1
            if temp > max_sum:
                max_sum = temp
        return max_sum / k
    

def test():
    s = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    print(s.findMaxAverage(nums, 6))
    

if __name__ == '__main__':
    test()