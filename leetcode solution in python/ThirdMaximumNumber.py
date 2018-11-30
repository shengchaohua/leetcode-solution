# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:00:59 2018

@problem: leetcode 414. Third Maximum Number

@author: shengchaohua
"""

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)
        
        nums = list(set(nums))
        front = nums[:3]
        front.sort()
        third_m, second_m, m = front[0], front[1], front[2]
        
        for num in nums[3:]:
            if num > third_m:
                third_m = num
                if third_m > second_m:
                    third_m, second_m = second_m, third_m
                    if second_m > m:
                        second_m, m = m, second_m
                        
        return third_m
    
        # Solution given by @waigx
#        a = b = c = -float("inf")
#        for n in nums:
#            if n in (a, b, c): continue
#            if n > a:
#                n, a = a, n
#            if n > b:
#                n, b = b, n
#            if n > c:
#                n, c = c, n
#        return a if c == -float("inf") else c
    
    
def test():
    s = Solution()
    nums = [1,2,3,4,5,5,6,6,6,6,7,7]
    print(s.thirdMax(nums))
    
    
if __name__ == '__main__':
    test()