# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:18:10 2018

@problem: leetcode 925. Long Pressed Name

@author: shengchaohua
"""

class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(typed) < len(name):
            return False
            
        i = j = 0
        while i < len(name) and j < len(typed):
            count = 1
            while i < len(name)-1 and name[i] == name[i+1]:
                i += 1
                count += 1
            while j < len(typed) and typed[j] == name[i]:
                j += 1
                count -= 1
                
            if count > 0:
                return False
            i += 1
        
        return i == len(name) and j == len(typed)
    
    
def test():
    s = Solution()
    name = "alex"
    typed = "aaleex"
    print(s.isLongPressedName(name, typed))
    
    name = "saeed"
    typed = "ssaaedd"
    print(s.isLongPressedName(name, typed))
    

if __name__ == '__main__':
    test()