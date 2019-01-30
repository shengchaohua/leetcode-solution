# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:41:33 2019

@problem: leetcode 680. Valid Palindrome II

@author: shengchaohua
"""

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def valid(s):
            left, right = 0, len(s)-1
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            return left >= right
        
        left, right = 0, len(s)-1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return valid(s[left+1:right+1]) or valid(s[left:right])
    

def test():
    s = Solution()
    print(s.validPalindrome('abc'))
    

if __name__ == '__main__':
    test()
    