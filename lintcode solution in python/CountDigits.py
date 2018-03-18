# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 20:40:55 2018

@problem: lintcode No.3 统计数字

@author: sheng
"""

class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        num = 0
        for i in range(n+1):
            num += str(i).count(str(k))
        return num

def main():
    s = Solution()
    print(s.digitCounts(1, 12))
    
if __name__ == '__main__':
    main()