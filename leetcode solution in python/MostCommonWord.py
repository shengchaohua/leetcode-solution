# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:48:17 2019

@problem: leetcode 819. Most Common Word

@author: shengchaohua
"""

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections
        banned = set(banned)
        words = []
        i = 0
        while i < len(paragraph):
            j = i
            while j < len(paragraph) and paragraph[j] not in "!?',;. ":
                j += 1
            s = paragraph[i:j].lower()
            if s not in banned: words.append(s)
            while j < len(paragraph) and paragraph[j] in "!?',;. ":
                j += 1
            i = j
        
        words_freq = collections.Counter(words)
        res = ('', 0)
        for w, num in words_freq.items():
            if num > res[1]:
                res = (w, num)
        return res[0]
        
    
def test():
    s = Solution()
    para = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    print(s.mostCommonWord(para, banned))
    
    
if __name__ == '__main__':
    test()
    