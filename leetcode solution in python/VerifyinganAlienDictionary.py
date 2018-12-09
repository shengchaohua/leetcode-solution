# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:39:41 2018

@problem: leetcode 953. Verifying an Alien Dictionary

@author: shengchaohua
"""

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        length = len(words)
        for i in range(length-1):
            for j in range(i+1, length):
                if self.cmp(words[i], words[j], order) == 1:
                    return False
        return True
        
    def cmp(self, w1, w2, order):
        '''If w1 > w2, return 1. Otherwise, return -1.'''
        i = 0
        while i < len(w1) and i < len(w2) and w1[i] == w2[i]:
            i += 1
            
        if i == len(w1): # w1 is smaller
            return -1
        if i == len(w2): # w1 is bigger
            return 1
        
        return 1 if order.index(w1[i]) > order.index(w2[i]) else -1
    
    
def test():
    s = Solution()
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(s.isAlienSorted(words, order))
    

if __name__ == '__main__':
    test()
            