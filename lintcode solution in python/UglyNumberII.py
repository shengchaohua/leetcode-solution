# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 20:47:53 2018

@problem: lintcode No.4 Ugly Number

@author: sheng
"""

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        # time exceed
#        l = [1, 2, 3, 4, 5]
#        while len(l) < n:
#            l1 = list(map(lambda x: 2*x, l))
#            l2 = list(map(lambda x: 3*x, l))
#            l3 = list(map(lambda x: 5*x, l))
#            sumL = l1 + l2 + l3
#            reducedL = [ele for ele in sumL if ele not in l]
#            l.append(min(reducedL))
#        return l[n-1]
        l = [1]
        i2 = i3 = i5 = 0
        while len(l) < n:
            num2 , num3, num5 = l[i2]* 2, l[i3] * 3, l[i5] * 5
            num = min(num2, num3, num5)
            # 下面三个 if 还有去重的作用
            if num == num2:
                i2 += 1
            if num == num3:
                i3 += 1
            if num == num5:
                i5 += 1
            l.append(num)
        return l[-1]

            
def main():
    s = Solution()
    print(s.nthUglyNumber(599))
    
if __name__ == '__main__':
    main()
            