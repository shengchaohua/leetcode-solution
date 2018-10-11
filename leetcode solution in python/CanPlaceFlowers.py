# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:22:43 2018

@problem: leetcode 605. Can Place Flowers

@author: shengchaohua
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1:
            return flowerbed[0] & n == 0
        
        left, right = 0, len(flowerbed)-1
        temp = 0
        while left <= right and flowerbed[left] == 0: # 最前面的0
            temp += 1
            left += 1
        if left == right+1: # 如果全是0，直接遍历到末尾
            return n <= (temp+1) // 2
        n -= temp // 2
        
        temp = 0
        while right > left and flowerbed[right] == 0: # 最后面的0
            temp += 1
            right -= 1
        n -= temp // 2
            
        while left < right: # 中间的0
            while left < right and flowerbed[left] == 1:
                left += 1
            temp = 0
            while left < right and flowerbed[left] == 0:
                temp += 1
                left += 1
            n -= (temp-1) // 2
                
        return n <= 0
            
            
def test():
    s = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    print(s.canPlaceFlowers(flowerbed, 1))
    print(s.canPlaceFlowers(flowerbed, 2))
    
    flowerbed = [0]
    print(s.canPlaceFlowers(flowerbed, 0))
    print(s.canPlaceFlowers(flowerbed, 1))
    
    flowerbed = [0, 0, 0]
    print(s.canPlaceFlowers(flowerbed, 2))
    
    flowerbed = [0, 0, 1]
    print(s.canPlaceFlowers(flowerbed, 3))
    
    
if __name__ == '__main__':
    test()