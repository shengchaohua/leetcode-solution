# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:08:17 2018

@problem: leetcode 954. Array of Doubled Pairs

@author: shengchaohua
"""

class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        import collections
        cnt = collections.Counter(A)
        for a in sorted(A, key = abs):
            if cnt[a] and cnt[a * 2]:
                cnt[a] -= 1
                cnt[a * 2] -= 1  
        return all(cnt[a] == 0 for a in A)
    

def test():
    s = Solution()
    A = [4, -2, 2, -4]
    print(s.canReorderDoubled(A))
    B = [-1,4,6,8,-4,6,-6,3,-2,3,-3,-8]
    print(s.canReorderDoubled(B))
    
    
if __name__ == '__main__':
    test()