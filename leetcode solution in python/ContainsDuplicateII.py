# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:46:36 2018

@problem: leetcode 219. Contains Duplicate II

@author: shengchaohua
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """ 
        # Time Limit Exceeded
        i = 0
        while i < len(nums):
            temp = nums[i:i+k+1]
            if len(set(temp)) < len(temp):
                return True
            i += 1
        
        return False
    
    
    def containsNearbyDuplicate_hash(self, nums, k):
        # AC!
        if k + 1 >= len(nums):
            return len(set(nums)) != len(nums)
        
        s = set(nums[0:k+1])
        i = 0
        for n in nums[k+1:]:
            s.remove(nums[i])
            i += 1
            if n in s:
                return True
            s.add(n)
        
        return False        
        
    
def test():
    s = Solution()
    nums = [1, 2, 3, 1]
    print(s.containsNearbyDuplicate(nums, 3))
    print(s.containsNearbyDuplicate_hash(nums, 3))
    
    nums = [1, 0, 1, 1]
    print(s.containsNearbyDuplicate(nums, 1))
    print(s.containsNearbyDuplicate_hash(nums, 1))
    
    nums = [1, 2, 3, 1, 2, 3]
    print(s.containsNearbyDuplicate(nums, 2))
    print(s.containsNearbyDuplicate_hash(nums, 2))
    
    nums = [99, 99]
    print(s.containsNearbyDuplicate(nums, 2))
    print(s.containsNearbyDuplicate_hash(nums, 2))
    
if __name__ == '__main__':
    test()