# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:38:47 2019

@problem: leetcode 438. Find All Anagrams in a String

@author: shengchaohua
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Time Limit Exceed!
        if len(p) > len(s):
            return []
        import collections
        freq = collections.Counter(p)
        
        res = []
        i = 0
        while i < len(s)-len(p)+1:
            temp = freq.copy()
            j = 0
            while j < len(p):
                if s[i + j] not in temp:
                    i += j + 1
                    break
                elif temp[s[i + j]] <= 0:
                    i += 1
                    break
                else:
                    temp[s[i + j]] -= 1
                    j += 1
            if j == len(p):
                res.append(i)
                i += 1
        
        return res
    

def test():
    s = Solution()
    print(s.findAnagrams('cbaebabacd', 'abc'))
    

if __name__ == '__main__':
    test()