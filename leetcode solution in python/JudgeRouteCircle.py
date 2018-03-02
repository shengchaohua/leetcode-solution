# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 20:31:25 2018

@problem: https://leetcode.com/problems/judge-route-circle/description/

@author: https://github.com/shengchaohua
"""

class JudgeRouteCircle:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        UDnum, LRnum = 0, 0
        for move in moves:
            if move == 'U':
                UDnum += 1
            elif move == 'D':
                UDnum -= 1
            elif move == 'L':
                LRnum += 1
            elif move == 'R':
                LRnum -= 1
        return UDnum == 0 and LRnum == 0

def main():
    test = JudgeRouteCircle()
    print(test.judgeCircle('LLLRRRUUUDD'))
    
if __name__ == '__main__':
    main()