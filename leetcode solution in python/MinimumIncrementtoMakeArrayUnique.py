# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:16:31 2018

@problem: leetcode 945. Minimum Increment to Make Array Unique

@author: shengchaohua
"""

class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Time Limit Exceeded!
        s = set()
        total_incre= 0
        for num in A:
            incre = 0
            while num in s:
                incre += 1
                num += 1
            s.add(num)
            total_incre += incre
        return total_incre
    
    
    def minIncrementForUnique2(self, A):
        # Time Limit Exceeded again!
        d = {}
        for a in A:
            if a not in d:
                d[a] = A.count(a)
        
        total_incre= 0
        d_temp = d.copy()
        for key, value in d.items():
            while value > 1:
                incre = 0
                k = key
                while k in d_temp:
                    k += 1
                    incre += 1
                d_temp[k] = 1
                total_incre += incre
                value -= 1
                
        return total_incre
    
    
    def minIncrementForUnique3(self, A):
        res = need = 0
        for i in sorted(A):
            res += max(need - i, 0)
            need = max(need, i) + 1
        return res
    

def test():
    s = Solution()
    A = [1,2,2]
    print(s.minIncrementForUnique(A))
    print(s.minIncrementForUnique2(A))
    A = [3,2,1,2,1,7]
    print(s.minIncrementForUnique(A))
    print(s.minIncrementForUnique3(A))
    A = [2,2,2,1]
    print(s.minIncrementForUnique3(A))

if __name__ == '__main__':
    test()