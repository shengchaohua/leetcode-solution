# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 22:20:14 2018

@problem: 821. Shortest Distance to a Character

@author: shengchaohua
"""

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        letter_ind = {}
        for i, letter in enumerate(S):
            if letter in letter_ind:
                letter_ind[letter].append(i)
            else:
                letter_ind[letter] = [i]
            
        shortest_distance = []
        for i, letter in enumerate(S):
            s_d = 10000
            for C_ind in letter_ind[C]:
                pre_d = abs(i - C_ind)
                s_d = pre_d if pre_d <= s_d else s_d
            shortest_distance.append(s_d)
            
        return shortest_distance
    
def main():
    s = Solution()
    S = "loveleetcode"
    C = 'e'
    print(s.shortestToChar(S, C))
    
if __name__ == '__main__':
    main()
                
                
                    
                
            