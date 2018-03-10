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
        length = len(bits)
        if bits[length - 1] == 1:
            return False
        bits.pop()  
        oneNum = 0
        while True:
            if not bits:
                break
            bit = bits.pop()
            if bit == 1:
                oneNum += 1
                oneNum %= 2
            else:
                break
        return True if oneNum == 0 else False    
    
def main():
    bits = [1, 1, 0, 0, 0]
    sc = SpecialCharacters()
    print(sc.isOneBitCharacter(bits))

if __name__ == '__main__':
    main()