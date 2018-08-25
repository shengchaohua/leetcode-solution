# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 22:39:48 2018

@problem: leetcode No.867 Transpose Matrix

@author: shengchaohua
"""

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n_col = len(A[0])
        return [[row[i] for row in A] for i in range(n_col)]
    
def main():
    s = Solution()
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[1,2,3],[4,5,6]]
    print(s.transpose(A))
    print(s.transpose(B))
    
if __name__ == '__main__':
    main()