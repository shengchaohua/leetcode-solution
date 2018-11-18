# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:31:09 2018

@problem: leetcode 944. Delete Columns to Make Sorted

@author: shengchaohua
"""

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        len_str = len(A[0])
        for i in range(len_str):
            column_i = [s[i] for s in A]
            if sorted(column_i) != column_i:
                res += 1
                    
        return res
    
    
def test():
    s = Solution()
    A = ["cba","daf","ghi"]
    print(s.minDeletionSize(A))
    
    
if __name__ == '__main__':
    test()
    