# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 11:41:34 2019

@problem: leetcode 986. Interval List Intersections

@author: shengchaohua
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        res = []
        for a in A:
            for b in B:
                if a.end < b.start:
                    break
                elif a.start > b.end:
                    continue
                res.append([max(a.start, b.start), min(a.end, b.end)])
        return res