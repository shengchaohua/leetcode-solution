# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:42:45 2018

@problem: Given a binary array, find the maximum number of consecutive 1s in this array.

@website: https://leetcode.com/problems/max-consecutive-ones/description/

@author: shengchaohua
"""

class MaxConsecutiveOnes:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        sum = 0
        for num in nums:
            sum += num
            if num == 1:
                max = sum if sum >= max else max
            else:
                sum = 0
        return max

def main():
    mco = MaxConsecutiveOnes()
    print(mco.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1, 1]))
    
if __name__ == '__main__':
    main()