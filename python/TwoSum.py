class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 + num2 == target and j > i:
                    return [i,j]  
                else:
                     continue

def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 13
    print(solution.twoSum(nums, target))

if __name__ == '__main__':
    main()