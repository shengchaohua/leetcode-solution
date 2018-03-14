# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:32:35 2018

@problem: Leetcode No.697 Degree of an Array

@author: sheng
"""

class DegreeOfAnArray:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        c = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums): 
            first.setdefault(v, i)
            last[v] = i
        degree = max(c.values())
        return min(last[v] - first[v] + 1 for v in c if c[v] == degree)

def main():
    de = DegreeOfAnArray()
    print(de.findShortestSubArray([1, 2, 2, 3, 1]))
    
if __name__ == '__main__':
    main()