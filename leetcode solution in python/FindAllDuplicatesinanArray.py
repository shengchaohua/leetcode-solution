# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 10:02:49 2018

@problem: leetcode 442. Find All Duplicates in an Array

@author: shengchaohua
"""

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time:O(n) Space:O(n)
        count = [0] * len(nums)
        res = []
        for n in nums:
            if count[n-1] == 1:
                res.append(n)
            else:
                count[n-1] = 1
        return res
    
    def findDuplicates2(self, nums):
        # Time:O(n) Space:O(1)
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1 # 标识该数字是否出现过
        return res
    
    
def test():
    s = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDuplicates(nums))
    print(s.findDuplicates2(nums))
  
    
if __name__ == '__main__':
    test()