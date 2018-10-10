# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 10:12:39 2018

@problem: Leetcode No.217 Contains Duplicate

@author: shengchaohua
"""

class ContainsDuplicate:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
    
    
    def containsDuplicate_hash(self, nums):
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
        
    
def main():
    cd = ContainsDuplicate()
    print(cd.containsDuplicate([1,2,3,4,4]))
    print(cd.containsDuplicate_hash([1,2,3,4,4]))
    
if __name__ == '__main__':
    main()