# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:18:37 2018

@problem: Leetcode No.561 Array Partition I

@author: sheng
"""

class ArrayPartitionI:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res
    
def main():
    ap = ArrayPartitionI()
    print(ap.arrayPairSum([1,4,3,2]))
    
if __name__ == '__main__':
    main()