# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:30:39 2019

@problem: leetcode 400. Nth Digit

@author: shengchaohua
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while True:
            num_i = 9 * i * 10 ** (i - 1)
            if n <= num_i:
                break
            n -= num_i
            i += 1
        
        res = []
        n_digits = i
        while i - 1 >= 0:
            (no, r) = divmod(n - 1, n_digits * 10 ** (i - 1))
            if i == n_digits:
                res.append(no + 1)
            else:
                res.append(no)
            n = r + 1
            i -= 1
        res.append(n)
                        
        return res[n - 1]
    
def test():
    s = Solution()
    print(s.findNthDigit(29))
    

if __name__ == '__main__':
    test()
    