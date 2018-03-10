# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:59:17 2018

@problem: Given a 32-bit signed integer, reverse digits of an integer.

@website: https://leetcode.com/problems/reverse-integer/description/

@author: shengchaohua
"""

class ReverseInteger(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x;
        res = 0
        for i, chr in enumerate(str(x)):
            res = res + int(chr) * (10 ** i)
            if res - 2 ** 31 > -1:
                return 0
        return -res if isNegative else res
    
def main():
    ri = ReverseInteger()
    for num in [123, -123, 0, 100, -100, 1563847412]:
        print(ri.reverse(num))
        
if __name__ == '__main__':
    main()
    
    
        
            
        