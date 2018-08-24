# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:04:54 2018

@problem: leetcode No.852 Peak Index in a Mountain A

@author: shengchaohua
"""

class Solution:
    def peakIndexInMountainA(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start, end = 0, len(A)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid-1] < A[mid] and A[mid] < A[mid+1]:
                start = mid
            elif A[mid-1] > A[mid] and A[mid] > A[mid+1]:
                end = mid
            else:
                return mid     
            
def main():
    s = Solution()
    A = [1, 2, 3, 4, 3, 2]
    print(s.peakIndexInMountainA(A))
    
if __name__ == '__main__':
    main()
         