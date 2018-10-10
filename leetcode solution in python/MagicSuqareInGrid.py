# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 18:51:55 2018

@problem: leetcode 840. Magic Squares In Grid

@author: shengchaohua
"""

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        num = 0
        for row in range(1, len(grid)-1):
            for col in range(1, len(grid[0])-1):
                if grid[row][col] == 5 and \
                max(grid[row-1][col-1:col+2]) < 10 and \
                max(grid[row][col-1:col+2]) < 10 and \
                max(grid[row+1][col-1:col+2]) < 10:
                    if sum(grid[row-1][col-1:col+2]) == 15 and \
                    sum(grid[row][col-1:col+2]) == 15 and \
                    sum(grid[row+1][col-1:col+2]) == 15 and \
                    grid[row-1][col-1] + grid[row+1][col+1] == 10 and \
                    grid[row-1][col] + grid[row+1][col] == 10 and \
                    grid[row-1][col+1] + grid[row+1][col-1] == 10:
                        num += 1
                    
        return num
    
    
def test():
    s = Solution()
    grid = [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    print(s.numMagicSquaresInside(grid))
    
    grid = [[1,8,6],
            [10,5,0],
            [4,2,9]]
    print(s.numMagicSquaresInside(grid))
    
    
if __name__ == '__main__':
    test()                  
                        