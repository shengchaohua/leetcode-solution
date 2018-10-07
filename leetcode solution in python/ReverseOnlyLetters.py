# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:29:53 2018

@problem: leetcode 917. Reverse Only Letters

@author: shengchaohua
"""

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        listS = list(S)
        left, right = 0, len(listS)-1
        while left < right:
            while left < right and not str.isalpha(listS[left]):
                left += 1
            while left < right and not str.isalpha(listS[right]):
                right -= 1
            listS[left], listS[right] = listS[right], listS[left]
            left += 1
            right -= 1
            
        return ''.join(listS)
    
    def reverseOnlyLetters2(self, S):
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(S[i])
        return "".join(ans)
    

def test():
    s = Solution()
    a = "ab-cd"
    print(s.reverseOnlyLetters(a))
    a = "a-bC-dEf-ghIj"
    print(s.reverseOnlyLetters(a))
    a = "Test1ng-Leet=code-Q!"
    print(s.reverseOnlyLetters(a))
    
    
if __name__ == '__main__':
    test()