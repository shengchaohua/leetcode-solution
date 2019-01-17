# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:42:45 2019

@problem: leetcode 883. Projection Area of 3D Shapes

@author: shengchaohua
"""

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid[0])
        xz = [max(row) for row in grid]
        yz = [max([row[i] for row in grid]) for i in range(N)]
        z = [1 for row in grid for r in row if r != 0]
        return sum(xz) + sum(yz) + sum(z)
    

def test():
    s = Solution()
    grid = [[1,2],[3,4]]
    print(s.projectionArea(grid))
    

if __name__ == '__main__':
    test()