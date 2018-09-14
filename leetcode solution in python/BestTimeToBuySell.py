# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 08:10:01 2018

@problem: leetcode 121. Best Time to Buy and Sell Stock

@author: shengchaohua
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time Limit Exceed
        max_profit = 0
        for i, num1 in enumerate(prices):
            for num2 in prices[i+1:]:
                if num2 < num1:
                    break
                else:
                    temp = num2 - num1
                    max_profit = temp if temp > max_profit else max_profit
        return max_profit
    
    
    def maxProfit2(self, prices):       
        min_price = 100000000000
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        
        return max_profit
        
        
def main():
    s = Solution()
    prices1 = [7,1,5,3,6,4,2,10]
    prices2 = [10,9,8,7,6,5,4,3,2,1,0]
    print(s.maxProfit(prices1), s.maxProfit2(prices1))
    print(s.maxProfit(prices2), s.maxProfit2(prices2))
    
if __name__ == '__main__':
    main()