# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 23:09:10 2018

@problem: lintcode 41. Maximum Subarray

@author: shengchaohua
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        # Problems again! My solution is right, but it can't AC!
        # The min sum of subArray is 0 because empty set([]) is a subarray.
        maxSum = 0
        temp = 0
        for num in nums:
            temp += num
            if temp < 0:
                temp = 0
            if temp > maxSum:
                maxSum = temp
        return maxSum
    
def main():
    s = Solution()
    print(s.maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
    
if __name__ == '__main__':
    main()