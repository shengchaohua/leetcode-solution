# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:46:43 2019

@problem: leetcode 748. Shortest Completing Word

@author: shengchaohua
"""

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
#        def is_right(w, lp_freq):
#            for c in w:
#                if c in lp_freq:
#                    lp_freq[c] -= 1
#            return all([v <= 0 for k, v in lp_freq.items()])
#        
#        import collections
#        reduced_lp = [c.lower() for c in licensePlate if c.isalpha()]
#        res = ('', 16)
#        for w in words:
#            lp_freq = collections.Counter(reduced_lp)
#            if is_right(w, lp_freq) and len(w) < res[1]:
#                res = (w, len(w))
#        return res[0]
    
        plate = [s.lower() for s in licensePlate if s.isalpha()]
        for word in sorted(words, key = len):
            temp = plate.copy()
            for c in word:
                if c in temp:
                    del temp[temp.index(c)]
            if len(temp) == 0:
                return word
        
    
def test():
    s = Solution()
    licensePlate = "1s3PSt"
    words = ["step", "steps", "stripe", "stepples"]
    print(s.shortestCompletingWord(licensePlate, words))
    

if __name__ == '__main__':
    test()
    
    