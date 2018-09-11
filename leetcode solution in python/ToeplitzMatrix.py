# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:04:31 2018

@problem: leetcode 766. Toeplitz Matrix

@author: shengchaohua
"""

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        for i in range(m-1):
            if matrix[i][0:-1] != matrix[i+1][1:]:
                return False
        return True
    
def main():
    s = Solution()
    matrix = [
      [1,2,3,4],
      [5,1,2,3],
      [9,5,1,2],
    ]
    print(s.isToeplitzMatrix(matrix))
    
if __name__ == '__main__':
    main()
            