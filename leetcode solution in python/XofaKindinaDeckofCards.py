# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:41:38 2018

@problem: leetcode 914. X of a Kind in a Deck of Cards

@author: shengchaohua
"""

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # brute force
        import collections
        deck_freq = collections.Counter(deck)
        unique_values = set(deck_freq.values())
        
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(freq % X == 0 for freq in unique_values):
                    return True
        
        return False
    
    
    def hasGroupsSizeX_gcd(self, deck):
        from fractions import gcd
        from functools import reduce
        import collections
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
    
    
def test():
    s = Solution()
    nums = [1,2,3,4,4,3,2,1]
    print(s.hasGroupsSizeX(nums))
    print(s.hasGroupsSizeX_gcd(nums))
    
    nums = [1,1,1,2,2,2,3,3]
    print(s.hasGroupsSizeX(nums))
    print(s.hasGroupsSizeX_gcd(nums))
    
    nums = [1]
    print(s.hasGroupsSizeX(nums))
    print(s.hasGroupsSizeX_gcd(nums))
    
    nums = [1,1]
    print(s.hasGroupsSizeX(nums))
    print(s.hasGroupsSizeX_gcd(nums))
    
    
if __name__ == '__main__':
    test()
    