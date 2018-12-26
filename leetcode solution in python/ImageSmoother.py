# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 10:23:18 2018

@problem: leetcode 661. Image Smoother

@author: shengchaohua
"""

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] //= count

        return ans
    

def test():
    s = Solution()
    M = [[1,1,1],
         [1,0,1],
         [1,1,1]]
    print(s.imageSmoother(M))
    

if __name__ == '__main__':
    test()
    