# -*- coding: utf-8 -*-
"""
@problem: leetcode Jian zhi offer 40. 最小的k个数

@author: shengchaohua
"""

class Solution:
    def getLeastNumbers(self, arr, k: int):
        def partition(arr, l, r):
            left = l
            right = r
            pivot = arr[l]
            while left < right:
                while left < right and arr[right] >= pivot:
                    right -= 1
                while left < right and arr[left] <= pivot:
                    left += 1
                if left != right:
                    arr[left], arr[right] = arr[right], arr[left]
            arr[left], arr[l] = arr[l], arr[left]
            return left

        def select(arr, l, r, k):
            if l < r:
                pos = partition(arr, l, r)
                #print(l, pos, r)
                num = pos - l + 1
                if k == num:
                    return
                elif k < num:
                     select(arr, l, pos - 1, k)
                else:
                     select(arr, pos + 1, r, k - num)

        if k >= len(arr):
            return arr
        select(arr, 0, len(arr)-1, k)
        return arr[:k]


def test():
    s = Solution()
    # nums = [3, 2, 1]
    # res = s.getLeastNumbers(nums, 2)
    nums = [0,1,1,2,4,4,1,3,3,2]
    res = s.getLeastNumbers(nums, 6)
    print(res)


if __name__ == '__main__':
    test()
