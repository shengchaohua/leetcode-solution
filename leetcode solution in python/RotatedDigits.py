# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:41:03 2019

@problem: leetcode 788. Rotated Digits

@author: shengchaohua
"""

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_valid(num):
            digits = []
            temp = num
            while temp > 0:
                (quo, res) = divmod(temp, 10)
                if res in (3, 4, 7):
                    return False
                digits.append(res)
                temp = quo
            for d in digits:
                if d in (2,5,6,9):
                    return True
            return False
    
        return sum([1 for num in range(1, N+1) if is_valid(num)])
                
    
def test():
    s = Solution()
    print(s.rotatedDigits(32))
    
    
if __name__ == '__main__':
    test()
    