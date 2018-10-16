# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:46:42 2018

@problem: leetcode 923. 3Sum With Multiplicity

@author: shengchaohua
"""

class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        # TLE
        length = len(A)
        num = 0
        i = 0
        while i < length - 2:
            if A[i] <= target:
                rest1 = target - A[i]
                j = i + 1
                while j < length - 1:
                    if A[j] <= rest1:
                        num += A[j+1:].count(rest1 - A[j])
                    j += 1               
            i += 1
        
        return num % (10**9 + 7)
    
    def threeSUmMulti_ThreePointer(slef, A, target):
        # TLE
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        for i, x in enumerate(A):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                # These steps differ:
                elif A[j] != A[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return int(ans)
    

def test():
    s = Solution()
    A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    print(s.threeSumMulti(A, 8))
    print(s.threeSUmMulti_ThreePointer(A, 8))
    
    A = [1, 1, 2, 2, 2, 2]
    print(s.threeSumMulti(A, 5))
    print(s.threeSUmMulti_ThreePointer(A, 5))
    
    A = [3, 3, 3, 0]
    print(s.threeSumMulti(A, 6))
    print(s.threeSUmMulti_ThreePointer(A, 6))
    
    A = [1, 3, 3, 0, 1]
    print(s.threeSumMulti(A, 4))
    print(s.threeSUmMulti_ThreePointer(A, 4))
    
    A = [1, 2, 0, 3, 2, 0, 0, 2, 1]
    print(s.threeSumMulti(A, 2))
    print(s.threeSUmMulti_ThreePointer(A, 2))
    
    A = [0] * 100
    print(s.threeSumMulti(A, 0))
    print(s.threeSUmMulti_ThreePointer(A, 0))
    
if __name__ == '__main__':
    test()
                      