# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 10:47:08 2018

@problem: leetcode 949. Largest Time for Given Digits

@author: shengchaohua
"""

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        import itertools
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02d}:{:02d}".format(*divmod(ans, 60)) if ans >= 0 else ""
    
    
def test():
    s = Solution()
    A = [1,2,3,4]
    print(s.largestTimeFromDigits(A))
            

if __name__ == '__main__':
    test()
        