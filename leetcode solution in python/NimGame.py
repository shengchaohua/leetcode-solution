# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 19:52:26 2018

@problem: https://leetcode.com/problems/nim-game/description/

@author: https://github.com/shengchaohua
"""

class NimGame:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
    
def main():
    ng = NimGame()
    print(ng.canWinNim(10))
    
if __name__ == '__main__':
    main()