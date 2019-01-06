# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:59:58 2019

@problem: leetcode 970. Powerful Integers

@author: shengchaohua
"""

class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if x == 1 and y == 1:
            return [2] if bound >= 2 else []
        elif x == 1:
            x, y = y, x
        
        res = set()
        i = 0
        while x ** i <= bound:
            residue = bound - x ** i
            j = 0
            while y ** j <= residue:
                if y == 1:
                    res.add(x**i + 1)
                    break
                res.add(x ** i + y ** j)
                j += 1
            i += 1
        
        return list(res)
    

def test():
    s = Solution()
    print(s.powerfulIntegers(5, 3, 15))
    

if __name__ == '__main__':
    test()