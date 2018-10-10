# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 08:29:10 2018

@problem: leetcode 849. Maximize Distance to Closest Person

@author: shengchaohua
"""

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dist = 0
        
        i = 0
        while i < len(seats) and seats[i] == 0:
            i += 1    
        max_dist = i
        
        while i < len(seats):
            while i < len(seats) and seats[i] == 1:
                i += 1
            left_person = i - 1
            
            while i < len(seats) and seats[i] == 0:
                i += 1
            right_person = i
            
            if right_person == len(seats): # 如果右边没有人
                temp_dist = right_person - left_person - 1
            else:
                temp_dist = (right_person - left_person) // 2
            
            if temp_dist > max_dist:
                max_dist = temp_dist
                
        return max_dist
            

def test():
    s = Solution()
    seats = [1, 0, 0, 0, 1, 0, 1]
    print(s.maxDistToClosest(seats))
    seats = [1, 0, 0, 0]
    print(s.maxDistToClosest(seats))
    
    
if __name__ == '__main__':
    test()