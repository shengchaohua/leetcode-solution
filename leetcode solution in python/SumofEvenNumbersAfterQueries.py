# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 11:06:46 2019

@problem: leetcode 985. Sum of Even Numbers After Queries

@author: shengchaohua
"""

class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        evens = [n for n in A if n % 2 == 0]
        even_sum = sum(evens) if evens else 0
        res = []
        for query in queries:
            val, idx = query[0], query[1]
            if A[idx] % 2 == 0 and val % 2 == 0:
                even_sum += val
                res.append(even_sum)
            elif A[idx] % 2 == 0 and val % 2 == 1:
                even_sum -= A[idx]
                res.append(even_sum)
            elif A[idx] % 2 == 1 and val % 2 == 1:
                even_sum += A[idx] + val
                res.append(even_sum)
            else:
                res.append(even_sum)
            A[idx] += val
        return res
    
    
def test():
    s = Solution()
    A = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    print(s.sumEvenAfterQueries(A, queries))
    

if __name__ == '__main__':
    test()