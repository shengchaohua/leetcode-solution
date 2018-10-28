# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:14:31 2018

@problem: leetcode 930. Binary Subarrays With Sum

@author: shengchaohua
"""

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # Brute solution but TLE!
        num = 0
        i = 0
        while i < len(A):                
            j = i
            temp = 0
            for k in range(j, len(A)):
                temp += A[k]
                if temp == S:
                    num += 1
                elif temp > S: 
                    break
            i += 1
        return num
    
    def numSubarraysWithSum1(self, A, S):
        '''Approach 1: Index of Ones'''
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in range(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i+1] - indexes[i] - 1
                ans += w * (w+1) / 2
            return int(ans)

        for i in range(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i-1]
            right = indexes[j+1] - indexes[j]
            ans += left * right
        
        return ans
    
    def numSubarraysWithSum2(self, A, S):
        '''Approach 2: Prefix Sums'''
        import collections
        prefix_sum = [0]
        for x in A:
            prefix_sum.append(prefix_sum[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in prefix_sum:
            ans += count[x]
            count[x + S] += 1

        return ans
    
def test():
    s = Solution()
    A = [1, 0, 1, 0, 1]
    print(s.numSubarraysWithSum(A, 2))
    
    B = [0, 0, 0, 0, 0]
    print(s.numSubarraysWithSum1(B, 0))
    
    C = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    print(s.numSubarraysWithSum2(C, 3))
    
if __name__ == '__main__':
    test()