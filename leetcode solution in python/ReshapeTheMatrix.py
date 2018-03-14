# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:43:03 2018

@problem: Leetcode No.566 Reshape the Matrix

@author: sheng
"""

class ReshapeTheMatrix:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        from functools import reduce
        row = len(nums)
        column = len(nums[0])
        if r * c != row * column:
            return nums
        flattenNums = reduce(lambda x,y: x+y, nums)
        # flattenNums = sum(nums, []) 更方便
        
        numsIter = iter(flattenNums)
        res = []
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(next(numsIter))
            res.append(temp)
        
        return res
    
def main():
    rtm = ReshapeTheMatrix()
    print(rtm.matrixReshape([[1,2],[3,4]], 1, 4))
    print(rtm.matrixReshape([[1,2],[3,4]], 2, 4))
    print(rtm.matrixReshape([[1,2,3],[3,4,5]], 3, 2))

if __name__ == '__main__':
    main()