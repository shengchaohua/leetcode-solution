# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:10:21 2018

@problem: Leetcode No.717

@author: shengchaohua
"""

class SpecialCharacters:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rty
        """
        bits.pop()  
        oneNum = 0
        while bits:
            if bits.pop() == 1:
                oneNum += 1
                oneNum %= 2
            else:
                break
        return oneNum == 0  
    
def main():
    bits = [1, 1, 0, 0, 0]
    sc = SpecialCharacters()
    print(sc.isOneBitCharacter(bits))

if __name__ == '__main__':
    main()