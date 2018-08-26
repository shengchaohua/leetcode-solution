# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 09:20:46 2018

@problem: leetcode No.806 Number of Lines To Write String

@author: shengchaohua
"""

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lengthPerLine = 0
        totalLines = 1
        for letter in S:
            lengthPerLine = lengthPerLine + widths[ord(letter)-ord('a')]
            if lengthPerLine > 100:
                totalLines += 1
                lengthPerLine = widths[ord(letter)-ord('a')]
        return [totalLines, lengthPerLine]
    
def main():
    s = Solution()
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "abcdefghijklmnopqrstuvwxyz"
    print(s.numberOfLines(widths, S))
    
    widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "bbbcccdddaaa"
    print(s.numberOfLines(widths, S))

if __name__ == '__main__':
    main()