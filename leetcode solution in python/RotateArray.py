# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:30:09 2018

@problem: leetcode 189. Rotate Array

@author: shengchaohua
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
#        k %= len(nums)
#        for i in range(k):
#            nums.insert(0, nums.pop())
        k %= len(nums)
        self.__reverse(nums, 0, len(nums)-1)
        self.__reverse(nums, 0, k-1)
        self.__reverse(nums, k, len(nums)-1)
        
    def __reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        

def test():
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 3)
    print(nums)
    
    
if __name__ == '__main__':
    test()