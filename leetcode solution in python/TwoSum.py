# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 19:19:40 2018

@problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

@Example:Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].

@author: shengchaohua
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 + num2 == target and j > i:
                    return [i,j]  
                else:
                     continue

def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 13
    print(solution.twoSum(nums, target))

if __name__ == '__main__':
    main()