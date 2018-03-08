# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:33:13 2018

@problem: LeetCode No.283 Move Zeroes

@author: sheng
"""

class MoveZeroes:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i, num in enumerate(nums):
            if num != 0:
                continue;
            j = i
            while j < length and nums[j] == 0:
                j += 1
            if j < length:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        print(nums)

def main():
    nums = [0, 1, 0, 3, 12, 11, 0, 1, 2, 0]
    mz = MoveZeroes()
    mz.moveZeroes(nums)

if __name__ == '__main__':
    main()