# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:24:57 2018

@problem: leetcode 628. Maximum Product of Three Numbers

@author: shengchaohua
"""

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        
        min1 = min(nums) # first min num
        nums.remove(min1)
        min2 = min(nums) 
        max1 = max(nums) # first max num
        nums.remove(max1)
        max2 = max(nums)   
        nums.remove(max2)
        max3 = max(nums)
        
        if min1 * min2 * max3 * max2 * max1 == 0:
            if min1 == 0 or min2 == 0:
                return max3 * max2 * max1
            else:
                return min1 * min2 * max1
        
        res1 = min1 * min2 * max1
        res2 = max1 * max2 * max3
        
        return res1 if res1 > res2 else res2
    
def main():
    s = Solution()
    l = [1,2,3,4]
    print(s.maximumProduct(l))
    
if __name__ == '__main__':
    main()