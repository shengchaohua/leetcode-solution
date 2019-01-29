# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:30:17 2019

@problem: leetcode 475. Heaters

@author: shengchaohua
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
#        houses.sort()
#        heaters.sort()
#        
#        heaters_idx = []
#        i, j = 0, 0
#        while i < len(houses) and j < len(heaters):
#            if houses[i] == heaters[j]:
#                heaters_idx.append(i)
#                j += 1
#            i += 1
#            
#        radius = 0
#        for i, h in enumerate(heaters):
#            if i > 0:
#                pre_htr = heaters[i-1]
#                cur_htr = heaters[i]
#                mid_houses = houses[heaters_idx[i-1]:heaters_idx[i]+1]
#                
#                min_r = min(max(hp-pre_htr, cur_htr-hp) for hp in mid_houses)
#                print(min_r)
#                radius = max(radius, min_r)
#
#        if heaters_idx[0] != 0:
#            min_r = min(h - hp for hp in houses[:heaters_idx[0]])
#            radius = max(radius, min_r)
#        if heaters_idx[-1] != len(houses) - 1:
#            min_r = min(hp - heaters[-1] for hp in houses[heaters_idx[-1]+1:])
#            radius = max(radius, min_r)
#        
#        return radius
        
        # Solution from @StefanPochmann
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i+2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r
        
        
def test():
    s = Solution()
    houses, heaters = [1,2,3,4], [1,4]
    print(s.findRadius(houses, heaters))
    
    
if __name__ == '__main__':
    test()