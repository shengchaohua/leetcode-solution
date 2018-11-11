# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 10:49:03 2018

@problem: leetcode 937. Reorder Log Files

@author: shengchaohua
"""

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs, digit_logs = [], []
        for l in logs:
            splited = l.split(' ')
            if 97 <= ord(splited[1][0]) <= 122:
                letter_logs.append([l, splited[0], splited[1:]])
            else:
                digit_logs.append(l)
        letter_logs.sort(key=lambda l: l[1])
        letter_logs.sort(key=lambda l: l[2])
        
        return [x[0] for x in letter_logs] + digit_logs
    
    
def test():
    s = Solution()
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(s.reorderLogFiles(logs))
    
    logs = ["qi ir oo i", "cp vnzw i", "0 fkbikbts", "4 j trouka", "gn j q al", "5r w wgqc", "m8 x haje", "fg 28694 6", "i gf mwdoa", "ao 0850716"]
    print(s.reorderLogFiles(logs))
    
    
if __name__ == '__main__':
    test()