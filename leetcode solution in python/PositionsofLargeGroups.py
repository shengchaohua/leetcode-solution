# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 08:55:08 2018

@problem： leetcode 830. Positions of Large Groups

@author: shengchaohua
"""

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
#        if len(S) < 3:
#            return []
#        
#        res = []
#        temp = S[0]
#        i = 0
#        begin = 0
#        
#        while i < len(S):
#            while i < len(S) and S[i] == temp:
#                i += 1
#            
#            if i - begin >= 3:
#                res.append([begin, i-1])
#            
#            if i < len(S):            
#                begin = i
#                temp = S[i]
#        
#        return res
        
        # regex solution
        # return [[r.start(), r.end() - 1] for r in re.finditer(r'(\w)\1{2,}', S)]
        
        # concise solution
        i = 0
        res = []
        while i < len(S):
            j = i + 1
            while j < len(S) and S[j] == S[i]:
                j = j + 1
            if (j - i) > 2:
                res.append([i, j - 1])
            i = j
            
        return res
        

def main():
    s = Solution()
    S = "aaa"
    print(s.largeGroupPositions(S))

    
if __name__ == '__main__':
    main()