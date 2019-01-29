# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:03:48 2019

@problem: leetcode 443. String Compression

@author: shengchaohua
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        while i < len(chars):
            count = 1
            while i + 1 < len(chars) and chars[i + 1] == chars[i]:
                count += 1
                chars.pop(i + 1)
            if count == 1:
                i += 1
            else:
                i += 1
                s = str(count)
                for c in s:
                    chars.insert(i, c)
                    i += 1
        
        print(chars)
        return len(chars)
    
    
def test():
    s = Solution()
    chars = ["a","a","b","b","c","c","c"]
    print(s.compress(chars))
    chars = ['a']
    print(s.compress(chars))
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(s.compress(chars))    
    
    
if __name__ == '__main__':
    test()
    