# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:53:47 2018

@problem: lintcode No.24 flatten list

@author: shengchaohua
"""

class Solution(object):
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        # Two lines below is not needed. Cuz there are wrong test cases.
        if isinstance(nestedList, int): # 两行不应该存在，该题有错误的测试用例10
            return [nestedList]
        while True:
            temp = []
            for r in nestedList:
                if isinstance(r, int):
                    temp.append(r)
                else:
                    temp.extend(r)
                nestedList = temp
            flag = True
            for r in nestedList:
                if isinstance(r, list):
                    flag = False
            if flag:
                break
        return nestedList

def main():
    s = Solution()
    print(s.flatten([10]))
    
if __name__ == '__main__':
    main()
                
