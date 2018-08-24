# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:40:03 2018

@problem: leetcode No.832 Flipping an Image

@author: shengchaohua
"""

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for row in A:
            row.reverse()
            res.append([1-x for x in row])
        return res
    
    def betterFlip(self, A):
        return [[1 ^ i for i in row[::-1]] for row in A]

def main():
    s = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(s.flipAndInvertImage(A))
    
if __name__ == '__main__':
    main()