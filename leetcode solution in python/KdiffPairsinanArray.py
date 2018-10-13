# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 08:50:27 2018

@problem: leetcode 532. K-diff Pairs in an Array

@author: shengchaohua
"""

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # AC!
        if len(nums) <= 1 or k < 0:
            return 0
        
        pairs = set()
        nums.sort()
        
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[j] - nums[i] == k:
                    pairs.add((nums[i], nums[j]))
                elif nums[j] - nums[i] > k:
                    break
                j += 1
                
        return len(pairs)
    
    
    def findPairs_set(self, nums, k):
        # TLE!
        if len(nums) <= 1 or k < 0:
            return 0
        
        pairs = set()
        temp_nums = nums.copy()
        for n in nums:
            temp_nums.remove(n)
            if n - k in temp_nums:
                pairs.add((n-k, n))
            if n + k in temp_nums:
                pairs.add((n, n+k))
            temp_nums.append(n)
        
        return len(pairs)
    
    
def test():
    s = Solution()
    nums = [3, 1, 4, 1, 5]
    print(s.findPairs(nums, 2))
    print(s.findPairs_set(nums, 2))
    
    nums = [1, 2, 3, 4, 5]
    print(s.findPairs(nums, 2))
    print(s.findPairs_set(nums, 2))
            
    nums = [1, 3, 1, 5, 4]
    print(s.findPairs(nums, 0))
    print(s.findPairs_set(nums, 0))
    
    
if __name__ == '__main__':
    test()