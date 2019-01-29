# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:08:40 2019

@problem: leetcode 459. Repeated Substring Pattern

@author: shengchaohua
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for size in range(1, length // 2 + 1): # pattern_size
            if length % size == 0:
                pattern = s[:size]
                for j in range(size, length, size):
                    if pattern != s[j : j+size]:
                        break
                else:
                    return True
        return False


def test():
    s = Solution()
    string = 'aba'
    print(s.repeatedSubstringPattern(string))
    
    
if __name__ == '__main__':
    test()